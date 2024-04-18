/********************************************************************************
 * Copyright (c) 2023 CEA-List
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0.
 *
 * SPDX-License-Identifier: EPL-2.0
 *
 ********************************************************************************/

#include <fmt/format.h>

#include "aidge/scheduler/MemoryManager.hpp"
#include "aidge/utils/ErrorHandling.hpp"

Aidge::MemoryManager::~MemoryManager() noexcept = default;

std::shared_ptr<Aidge::MemoryManager::MemorySpace> Aidge::MemoryManager::reserve(
    unsigned int size,
    const std::set<std::shared_ptr<Node> >& dependencies)
{
    const unsigned int offset = onStack(size);

    std::shared_ptr<MemorySpace> memSpace
        = std::make_shared<MemorySpace>(mClock, offset, size, dependencies);
    mMemSpaces.push_back(memSpace);
    return memSpace;
}

void Aidge::MemoryManager::expand(
    std::shared_ptr<MemorySpace> memSpace,
    unsigned int requiredSize)
{
    assert(std::find(mMemSpaces.begin(), mMemSpaces.end(), memSpace)
            != mMemSpaces.end());

    memSpace->size = std::max(memSpace->size, requiredSize);

    // Rebuild the stack from the beginning, taking into account the new size.
    // Everything else stay the same.
    mMemStack.clear();

    for (Clock_T clock = 0; clock <= mClock; ++clock) {
        for (std::vector<std::shared_ptr<MemorySpace> >::iterator
            it = mMemSpaces.begin(), itEnd = mMemSpaces.end(); it != itEnd;
            ++it)
        {
            if ((*it)->allocated == clock)
                (*it)->offset = onStack((*it)->size);
        }

        // MemorySpace released at clock are still valid until the next tick;
        // make sure offStack() only append after all onStack() are done.
        for (std::vector<std::shared_ptr<MemorySpace> >::iterator
            it = mMemSpaces.begin(), itEnd = mMemSpaces.end(); it != itEnd;
            ++it)
        {
            if ((*it)->released == clock && (*it)->dependencies.empty())
                offStack((*it)->offset);
        }
    }
}

Aidge::MemoryManager::MemoryPlane Aidge::MemoryManager::allocate(
    unsigned int size,
    const std::set<std::shared_ptr<Node> >& dependencies,
    unsigned int stride,
    unsigned int length,
    unsigned int count)
{
    const unsigned int fullSize = std::max(size, stride) * length * count;
    return MemoryPlane(reserve(fullSize, dependencies),
                       mClock, 0, size, stride, length, count);
}

unsigned int Aidge::MemoryManager::allocate(
    const std::shared_ptr<Node>& node,
    unsigned int size,
    const std::set<std::shared_ptr<Node> >& dependencies,
    unsigned int stride,
    unsigned int length,
    unsigned int count)
{
    std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >::iterator it;
    std::tie(it, std::ignore) = mMemPlanes.insert(std::make_pair(node,
                                                std::vector<MemoryPlane>()));

    (*it).second.push_back(allocate(size, dependencies, stride, length, count));
    return ((*it).second.size() - 1);
}

bool Aidge::MemoryManager::isWrapAround(
    std::shared_ptr<MemorySpace> memSpace,
    unsigned int offset,
    unsigned int size,
    unsigned int stride,
    unsigned int length,
    unsigned int count) const
{
    const unsigned int fullSize = std::max(size, stride) * length * count;
    return (offset + fullSize > memSpace->size);
}

Aidge::MemoryManager::MemoryPlane Aidge::MemoryManager::reallocate(
    std::shared_ptr<MemorySpace> memSpace,
    unsigned int offset,
    unsigned int size,
    bool wrapAround,
    unsigned int extraSize,
    const std::set<std::shared_ptr<Node> >& additionalDependencies,
    unsigned int stride,
    unsigned int length,
    unsigned int count)
{
    const unsigned int fullSize = std::max(size, stride) * length * count;
    unsigned int requiredSize = offset + fullSize;

    if (wrapAround) {
        requiredSize = fullSize + extraSize;

        if (count > 1) {
            // (requiredSize - offset) must be a multiple of (stride * length)
            requiredSize = offset
                + std::ceil((requiredSize - offset)
                    / static_cast<double>(std::max(size, stride) * length))
                        * (std::max(size, stride) * length);
        }
        else if (length > 1) {
            // (requiredSize - offset) must be a multiple of stride
            requiredSize = offset
                + std::ceil((requiredSize - offset)
                    / static_cast<double>(std::max(size, stride)))
                        * std::max(size, stride);
        }
    }

    if (requiredSize > memSpace->size || memSpace->released >= 0) {
        // Expand in size and/or duration.
        // If memSpace was already released, put it back on the stack
        memSpace->released = -1;
        expand(memSpace, requiredSize);
    }

    memSpace->dependencies.insert(additionalDependencies.begin(),
                                  additionalDependencies.end());

    return MemoryPlane(memSpace, mClock, offset, size, stride, length, count);
}

Aidge::MemoryManager::MemoryPlane Aidge::MemoryManager::reallocate(
    const MemoryPlane& memPlane,
    unsigned int extraOffset,
    unsigned int size,
    bool wrapAround,
    unsigned int extraSize,
    const std::set<std::shared_ptr<Node> >& additionalDependencies,
    unsigned int stride,
    unsigned int length,
    unsigned int count)
{
    const unsigned int initialOffset = memPlane.getFinalOffset()
        - memPlane.memSpace->offset + extraOffset;
    const unsigned int fullSize = std::max(size, stride) * length * count;
    unsigned int requiredSize = initialOffset + fullSize;

    if (wrapAround) {
        requiredSize = fullSize + extraSize;

        if (count > 1) {
            // (requiredSize - offset) must be a multiple of (stride * length)
            requiredSize = initialOffset
                + std::ceil((requiredSize - initialOffset)
                    / static_cast<double>(std::max(size, stride) * length))
                        * (std::max(size, stride) * length);
        }
        else if (length > 1) {
            // (requiredSize - offset) must be a multiple of stride
            requiredSize = initialOffset
                + std::ceil((requiredSize - initialOffset)
                    / static_cast<double>(std::max(size, stride)))
                        * std::max(size, stride);
        }

        // Make sure that the intended margin with previous memPlane will be
        // respected, as it may actually be lower because of the floor()
        // in the memPlane getLimit() function.
        if (memPlane.count > 1) {
            requiredSize = memPlane.offset
                + std::ceil((requiredSize - memPlane.offset)
                    / static_cast<double>(memPlane.stride * memPlane.length))
                        * (memPlane.stride * memPlane.length);
        }
        else if (memPlane.length > 1) {
            requiredSize = memPlane.offset
                + std::ceil((requiredSize - memPlane.offset)
                    / static_cast<double>(memPlane.stride))
                        * memPlane.stride;
        }
    }

    if (requiredSize > memPlane.memSpace->size
        || memPlane.memSpace->released >= 0)
    {
        // Expand in size and/or duration.
        // If memSpace was already released, put it back on the stack
        memPlane.memSpace->released = -1;
        expand(memPlane.memSpace, requiredSize);
    }

    memPlane.memSpace->dependencies.insert(
        additionalDependencies.begin(),
        additionalDependencies.end());

    const unsigned int finalOffset = memPlane.getFinalOffset()
        - memPlane.memSpace->offset + extraOffset;

    return MemoryPlane(memPlane.memSpace, mClock,
                       finalOffset, size, stride, length, count);
}

unsigned int Aidge::MemoryManager::reallocate(
    const MemoryPlane& memPlane,
    const std::shared_ptr<Node>& node,
    unsigned int extraOffset,
    unsigned int size,
    bool wrapAround,
    unsigned int extraSize,
    const std::set<std::shared_ptr<Node> >& additionalDependencies,
    unsigned int stride,
    unsigned int length,
    unsigned int count)
{
    std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >::iterator it;
    std::tie(it, std::ignore) = mMemPlanes.insert(std::make_pair(node,
                                                std::vector<MemoryPlane>()));

    (*it).second.push_back(reallocate(memPlane, extraOffset, size, wrapAround,
                                      extraSize, additionalDependencies,
                                      stride, length, count));
    return ((*it).second.size() - 1);
}

unsigned int Aidge::MemoryManager::reallocate(
    std::shared_ptr<MemorySpace> memSpace,
    const std::shared_ptr<Node>& node,
    unsigned int offset,
    unsigned int size,
    bool wrapAround,
    unsigned int extraSize,
    const std::set<std::shared_ptr<Node> >& additionalDependencies,
    unsigned int stride,
    unsigned int length,
    unsigned int count)
{
    std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >::iterator it;
    std::tie(it, std::ignore) = mMemPlanes.insert(std::make_pair(node,
                                                std::vector<MemoryPlane>()));

    (*it).second.push_back(reallocate(memSpace, offset, size, wrapAround,
                                      extraSize, additionalDependencies,
                                      stride, length, count));
    return ((*it).second.size() - 1);
}

unsigned int Aidge::MemoryManager::release(std::shared_ptr<MemorySpace> memSpace)
{
    if (memSpace->released == -1) {
        memSpace->released = mClock;

        if (memSpace->dependencies.empty())
            return offStack(memSpace->offset);
    }

    return 0;
}

unsigned int Aidge::MemoryManager::release(const std::shared_ptr<Node>& node)
{
    const std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::iterator it = mMemPlanes.find(node);

    if (it == mMemPlanes.end()) {
        fmt::print("Warning: release(): there is no allocated memory for node {}\n", node->name());
        return 0;
    }

    unsigned int releasedMemSize = 0;

    for (std::vector<MemoryPlane>::iterator itPlanes = (*it).second.begin(),
        itPlanesEnd = (*it).second.end(); itPlanes != itPlanesEnd; ++itPlanes)
    {
        releasedMemSize += release((*itPlanes).memSpace);
    }

    // Remove dependencies
    releasedMemSize += releaseDependencies(node);

    return releasedMemSize;
}

unsigned int Aidge::MemoryManager::releaseDependencies(
    const std::shared_ptr<Node>& node)
{
    unsigned int releasedMemSize = 0;

    for (std::vector<std::shared_ptr<MemorySpace> >::iterator
        it = mMemSpaces.begin(), itEnd = mMemSpaces.end(); it != itEnd;
        ++it)
    {
        if (!(*it)->dependencies.empty()) {
            (*it)->dependencies.erase(node);

            if ((*it)->released <= mClock
                && (*it)->dependencies.empty())
            {
                (*it)->released = mClock;
                releasedMemSize += offStack((*it)->offset);
            }
        }
    }

    return releasedMemSize;
}

bool Aidge::MemoryManager::MaxLifetimeMinSizeFirst::operator()(
    const std::shared_ptr<MemorySpace>& p0,
    const std::shared_ptr<MemorySpace>& p1)
{
    const Clock_T lifetime0
        = ((p0->released >= 0) ? p0->released : maxLifetime) - p0->allocated;
    const Clock_T lifetime1
        = ((p1->released >= 0) ? p1->released : maxLifetime) - p1->allocated;

    return (lifetime0 > lifetime1
            || (lifetime0 == lifetime1 && p0->size < p1->size));
}

bool Aidge::MemoryManager::MaxLifetimeMaxSizeFirst::operator()(
    const std::shared_ptr<MemorySpace>& p0,
    const std::shared_ptr<MemorySpace>& p1)
{
    const Clock_T lifetime0
        = ((p0->released >= 0) ? p0->released : maxLifetime) - p0->allocated;
    const Clock_T lifetime1
        = ((p1->released >= 0) ? p1->released : maxLifetime) - p1->allocated;

    return (lifetime0 > lifetime1
            || (lifetime0 == lifetime1 && p0->size > p1->size));
}

bool Aidge::MemoryManager::MaxHoleMaxLifetimeFirst::operator()(
    const std::shared_ptr<MemorySpace>& p0,
    const std::shared_ptr<MemorySpace>& p1)
{
    const Clock_T lifetime0
        = ((p0->released >= 0) ? p0->released : maxLifetime) - p0->allocated;
    const Clock_T lifetime1
        = ((p1->released >= 0) ? p1->released : maxLifetime) - p1->allocated;

    const std::pair<Clock_T, unsigned int> maxHole0 = inst->getMaxHole(p0);
    const std::pair<Clock_T, unsigned int> maxHole1 = inst->getMaxHole(p1);

    return (maxHole0.second > maxHole1.second
            || (maxHole0.second == maxHole1.second && lifetime0 > lifetime1));
}

void Aidge::MemoryManager::optimize(OptimizeStrategy strategy) {
    if (strategy == None)
        return;

    const unsigned int maxLifetime = getMaxLifetime();

    if (strategy == OptimizeMaxLifetimeMinSizeFirst) {
        std::stable_sort(mMemSpaces.begin(), mMemSpaces.end(),
                        MemoryManager::MaxLifetimeMinSizeFirst(maxLifetime));
    }
    else if (strategy == OptimizeMaxLifetimeMaxSizeFirst) {
        std::stable_sort(mMemSpaces.begin(), mMemSpaces.end(),
                        MemoryManager::MaxLifetimeMaxSizeFirst(maxLifetime));
    }
    else if (strategy == OptimizeMaxHoleMaxLifetimeFirst) {
        std::stable_sort(mMemSpaces.begin(), mMemSpaces.end(),
                        MemoryManager::MaxHoleMaxLifetimeFirst(maxLifetime, this));
    }

    std::vector<std::map<unsigned int, unsigned int> > stacks(maxLifetime + 1,
                                        std::map<unsigned int, unsigned int>());

    for (std::vector<std::shared_ptr<MemorySpace> >::const_iterator
        it = mMemSpaces.begin(), itEnd = mMemSpaces.end(); it != itEnd; ++it)
    {
        const Clock_T maxT = ((*it)->released >= 0
                                && (*it)->dependencies.empty())
                                    ? (*it)->released : maxLifetime;

        // Merge stacks over memSpace lifetime
        std::map<unsigned int, unsigned int> mergedStacks;

        for (Clock_T t = (*it)->allocated; t <= maxT; ++t) {
            for (std::map<unsigned int, unsigned int>::iterator itMem
                = stacks[t].begin(), itMemEnd = stacks[t].end();
                itMem != itMemEnd; ++itMem)
            {
                bool newInsert;
                std::map<unsigned int, unsigned int>::iterator itMergedMem;
                std::tie(itMergedMem, newInsert) = mergedStacks.insert(
                    std::make_pair((*itMem).first, (*itMem).second));

                if (!newInsert) {
                    (*itMergedMem).second = std::max((*itMergedMem).second,
                                                     (*itMem).second);
                }
            }
        }

        std::map<unsigned int, unsigned int> mergedStack;

        if (!mergedStacks.empty()) {
            std::map<unsigned int, unsigned int>::iterator itMem
                = mergedStacks.begin();

            mergedStack.insert(*itMem);
            ++itMem;

            while (itMem != mergedStacks.end()) {
                std::map<unsigned int, unsigned int>::reverse_iterator
                    itMergedMem = mergedStack.rbegin();
                const unsigned int nextOffset = (*itMergedMem).first
                                                + (*itMergedMem).second;

                if ((*itMem).first <= nextOffset) {
                    (*itMergedMem).second
                        = std::max((*itMem).first + (*itMem).second, nextOffset)
                            - (*itMergedMem).first;
                }
                else
                    mergedStack.insert(*itMem);

                ++itMem;
            }
        }

        // Allocate in merged stack
        unsigned int offset = 0;
        std::map<unsigned int, unsigned int>::iterator itMem
            = mergedStack.begin();

        while (true) {
            if (itMem == mergedStack.end()
                || (*itMem).first - offset >= (*it)->size)
            {
                mergedStack.insert(std::make_pair(offset, (*it)->size));
                break;
            }
            else {
                offset = (*itMem).first + (*itMem).second;
                ++itMem;
            }
        }

        (*it)->offset = offset;

        for (Clock_T t = (*it)->allocated; t <= maxT; ++t) {
            const std::map<unsigned int, unsigned int> stack
                = getStack((*it), t);
            stacks[t].insert(stack.begin(), stack.end());

            //stacks[t].insert(std::make_pair(offset, (*it)->size));
        }
    }
}

unsigned int Aidge::MemoryManager::getOffset(const std::shared_ptr<Node>& node,
                                            unsigned int plane) const
{
    const std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator it = mMemPlanes.find(node);

    if (it == mMemPlanes.end()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "getOffset(): no memory allocated for node name {}", node->name());
    }

    if (plane >= (*it).second.size()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "getOffset(): plane out of range for node name {}", node->name());
    }

    return ((*it).second[plane].memSpace->offset + (*it).second[plane].offset);
}

unsigned int Aidge::MemoryManager::getSize(const std::shared_ptr<Node>& node,
                                          unsigned int plane) const
{
    const std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator it = mMemPlanes.find(node);

    if (it == mMemPlanes.end()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "getSize(): no memory allocated for node name {}", node->name());
    }

    if (plane >= (*it).second.size()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "getSize(): plane out of range for node name {}", node->name());
    }

    return (*it).second[plane].getSize();
}

unsigned int Aidge::MemoryManager::getSize(const std::shared_ptr<Node>& node)
    const
{
    const std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator it = mMemPlanes.find(node);

    if (it == mMemPlanes.end()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "getSize(): no memory allocated for node name {}", node->name());
    }

    unsigned int size = 0;

    for (std::vector<MemoryPlane>::const_iterator itPlanes
        = (*it).second.begin(), itPlanesEnd = (*it).second.end();
        itPlanes != itPlanesEnd; ++itPlanes)
    {
        size += (*itPlanes).getSize();
    }

    return size;
}

unsigned int Aidge::MemoryManager::getNbPlanes(const std::shared_ptr<Node>& node)
    const
{
    const std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator it = mMemPlanes.find(node);
    return (it == mMemPlanes.end()) ? 0 : (*it).second.size();
}

unsigned int Aidge::MemoryManager::getPeakUsage() const {
    unsigned int peakUsage = 0;

    for (std::vector<std::shared_ptr<MemorySpace> >::const_iterator
        it = mMemSpaces.begin(), itEnd = mMemSpaces.end(); it != itEnd; ++it)
    {
        peakUsage = std::max(peakUsage,
                             (*it)->offset + (*it)->size);
    }

    return peakUsage;
}

Aidge::MemoryManager::Clock_T Aidge::MemoryManager::getMaxLifetime() const {
    Clock_T maxLifetime = 0;

    for (std::vector<std::shared_ptr<MemorySpace> >::const_iterator
        it = mMemSpaces.begin(), itEnd = mMemSpaces.end(); it != itEnd; ++it)
    {
        maxLifetime = std::max(maxLifetime,
            std::max((*it)->allocated, (*it)->released));
    }

    return maxLifetime;
}

const std::vector<Aidge::MemoryManager::MemoryPlane>&
Aidge::MemoryManager::getPlanes(const std::shared_ptr<Node>& node) const
{
    const std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator it = mMemPlanes.find(node);

    if (it == mMemPlanes.end()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "getSize(): no memory allocated for node name {}", node->name());
    }

    return (*it).second;
}

Aidge::MemoryManager::MemMap_T
Aidge::MemoryManager::getPlanes(std::shared_ptr<MemorySpace> memSpace)
    const
{
    MemMap_T planes;

    for (MemMap_T::const_iterator itNode = mMemPlanes.begin(),
        itNodeEnd = mMemPlanes.end(); itNode != itNodeEnd; ++itNode)
    {
        for (std::vector<MemoryPlane>::const_iterator itPlane
             = (*itNode).second.begin(), itPlaneEnd = (*itNode).second.end();
             itPlane != itPlaneEnd; ++itPlane)
        {
            if ((*itPlane).memSpace == memSpace) {
                std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
                    ::iterator it;
                std::tie(it, std::ignore) = planes.insert(
                    std::make_pair((*itNode).first,
                                   std::vector<MemoryPlane>()));

                (*it).second.push_back((*itPlane));
            }
        }
    }

    return planes;
}

unsigned int Aidge::MemoryManager::getNbPlanes(
    std::shared_ptr<MemorySpace> memSpace) const
{
    unsigned int count = 0;

    for (std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator itNode = mMemPlanes.begin(),
        itNodeEnd = mMemPlanes.end(); itNode != itNodeEnd; ++itNode)
    {
        for (std::vector<MemoryPlane>::const_iterator itPlane
             = (*itNode).second.begin(), itPlaneEnd = (*itNode).second.end();
             itPlane != itPlaneEnd; ++itPlane)
        {
            if ((*itPlane).memSpace == memSpace)
                ++count;
        }
    }

    return count;
}

void Aidge::MemoryManager::tick()
{
    ++mClock;
}

void Aidge::MemoryManager::log(const std::string& fileName) const
{
    auto memData = std::unique_ptr<FILE, decltype(&std::fclose)>(std::fopen(fileName.c_str(), "w"), &std::fclose);

    if (!memData) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "Could not create memory layout log file: {}", fileName);
    }

    auto gnuplot = std::unique_ptr<FILE, decltype(&std::fclose)>(std::fopen((fileName + "_plot.gnu").c_str(), "w"), &std::fclose);

    if (!gnuplot) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "Could not create memory layout log file: {}", (fileName + "_plot.gnu"));
    }

    const Clock_T maxLifetime = getMaxLifetime();
    const unsigned int peakUsage = getPeakUsage();

    fmt::print(gnuplot.get(), "#!/usr/bin/gnuplot\n");
    fmt::print(gnuplot.get(), "set term pngcairo size 1280,768 noenhanced\n");
    fmt::print(gnuplot.get(), "set output \"{}\"\n", fileName + "_plot.png");
    fmt::print(gnuplot.get(), "set xrange [{}:{}]\n", 0, maxLifetime + 1);
    fmt::print(gnuplot.get(), "set yrange [{}:{}]\n", 0, 1.05 * (peakUsage / 1024.0));
    fmt::print(gnuplot.get(), "set xlabel \"Time\"\n");
    fmt::print(gnuplot.get(), "set ylabel \"Memory usage (KWords)\"\n");
    fmt::print(gnuplot.get(), "set grid\n");
    fmt::print(gnuplot.get(), "set xtics 1\n");
    fmt::print(gnuplot.get(), "unset key\n");
    fmt::print(gnuplot.get(), "set palette rgbformulae 30,31,32\n");
    fmt::print(gnuplot.get(), "unset colorbox\n");
    fmt::print(gnuplot.get(), "N={}\n", mMemPlanes.size() + 1);

    unsigned int objectId = 1;
    unsigned int labelId = 1;

    for (std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator it = mMemPlanes.begin(), itEnd = mMemPlanes.end();
        it != itEnd; ++it)
    {
        const std::string name = (*it).first->name();
        fmt::print(memData.get(), "{}\n", name);

        double minX = -1;
        unsigned int maxY = 0;

        for (std::vector<MemoryPlane>::const_iterator itPlanes
             = (*it).second.begin(), itPlanesBegin = (*it).second.begin(),
            itPlanesEnd = (*it).second.end(); itPlanes != itPlanesEnd;
            ++itPlanes)
        {
            const unsigned int contiguousOffset
                = (*itPlanes).getContiguousOffset();
            const unsigned int contiguousSize = (*itPlanes).getContiguousSize();
            const unsigned int wrappedOffset = (*itPlanes).getWrappedOffset();
            const unsigned int wrappedSize = (*itPlanes).getWrappedSize();

            const Clock_T allocated = (*itPlanes).allocated;
            const Clock_T released = (*itPlanes).memSpace->released;
            const bool isReleased = (released >= 0
                                && (*itPlanes).memSpace->dependencies.empty());

            fmt::print(memData.get(), "  {} {} ({:#08x}U) -> {} ({:#08x}U)",
                (itPlanes - itPlanesBegin), contiguousOffset, contiguousOffset,
                (contiguousOffset + contiguousSize), (contiguousOffset + contiguousSize));

            if (wrappedSize > 0) {
                fmt::print(memData.get(), " + {} ({:#08x}U) -> {} ({:#08x}U)",
                    wrappedOffset, wrappedOffset,
                    (wrappedOffset + wrappedSize), (wrappedOffset + wrappedSize));
            }

            fmt::print(memData.get(), " [{}] @ {}", (*itPlanes).getSize(), allocated);

            if (isReleased) {
                fmt::print(memData.get(), " to {}", released);
            }

            fmt::print(memData.get(), "\n");

            // Gnuplot
            const double startX = allocated;

            if (startX < minX || minX < 0) {
                minX = startX;
                maxY = contiguousOffset + contiguousSize;
            }

            if ((*itPlanes).size != (*itPlanes).stride) {
                for (unsigned int offset = contiguousOffset;
                    offset < contiguousOffset + contiguousSize;
                    offset += (*itPlanes).stride)
                {
                    fmt::print(gnuplot.get(), "set object {} rectangle from {},{} to {},{} fc palette frac ({} * 1./N)\n",
                        (allocated * 100 + objectId), startX, (offset / 1024.0),
                        (((isReleased) ? released : maxLifetime) + 1),
                        (std::min((offset + (*itPlanes).size),
                                        contiguousOffset + contiguousSize) / 1024.0),
                        labelId);
                    ++objectId;
                }
            }
            else {
                fmt::print(gnuplot.get(), "set object {} rectangle from {},{} to {},{} fc palette frac ({} * 1./N)\n",
                    (allocated * 100 + objectId), startX, (contiguousOffset / 1024.0),
                    (((isReleased) ? released : maxLifetime) + 1),
                    ((contiguousOffset + contiguousSize) / 1024.0),
                    labelId);
                ++objectId;
            }

            if (wrappedSize > 0) {
                fmt::print(gnuplot.get(), "set object {} rectangle from {},{} to {},{} fc palette frac ({} * 1./N)\n",
                    (allocated * 100 + objectId), startX, (wrappedOffset / 1024.0),
                    (((isReleased) ? released : maxLifetime) + 1),
                    ((wrappedOffset + contiguousSize) / 1024.0),
                    labelId);
                ++objectId;

                fmt::print(gnuplot.get(), "set arrow from {},{} to {},{} nohead\n",
                    startX, (contiguousOffset / 1024.0),
                    (startX + 0.1), (contiguousOffset / 1024.0));

                fmt::print(gnuplot.get(), "set arrow from {},{} to {},{} nohead\n",
                    (startX + 0.05), ((contiguousOffset + contiguousSize) / 1024.0),
                    (startX + 0.05), (wrappedOffset / 1024.0));
            }
        }

        fmt::print(gnuplot.get(), "set label {} '{}' at {},{} rotate by 30 font \",8\" offset char 0.5,0.5\n",
            labelId, name, minX, (maxY / 1024.0));
        ++labelId;

        fmt::print(memData.get(), "\n");
    }

    fmt::print(gnuplot.get(), "set arrow from 0,{} to {},{} nohead lc rgb \"red\"\n",
        (peakUsage / 1024.0), (maxLifetime + 1),
        (peakUsage / 1024.0));

    fmt::print(gnuplot.get(), "set label {} 'Peak usage = {} KWords' at 0,{} textcolor rgb \"red\" offset char 0.5,0.5\n",
        labelId, (peakUsage / 1024.0), (peakUsage / 1024.0));

    fmt::print(gnuplot.get(), "plot 0\n");
}

unsigned int Aidge::MemoryManager::onStack(unsigned int size)
{
    unsigned int offset = 0;
    std::map<unsigned int, unsigned int>::iterator itMem = mMemStack.begin();

    while (true) {
        if (itMem == mMemStack.end()
            || (*itMem).first - offset >= size)
        {
            mMemStack.insert(std::make_pair(offset, size));
            break;
        }
        else {
            offset = (*itMem).first + (*itMem).second;
            ++itMem;
        }
    }

    return offset;
}

unsigned int Aidge::MemoryManager::offStack(unsigned int offset)
{
    std::map<unsigned int, unsigned int>::iterator itMem
        = mMemStack.find(offset);

    if (itMem == mMemStack.end()) {
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "offStack(): offset not found in stack");
    }
    else {
        const unsigned int size = (*itMem).second;
        mMemStack.erase(offset);
        return size;
    }
}

std::map<unsigned int, unsigned int> Aidge::MemoryManager::getStack(
    std::shared_ptr<MemorySpace> memSpace,
    Clock_T clock) const
{
    // Find all planes associated to memSpace and index them by their allocated
    // value in a map
    std::map<Clock_T, std::vector<MemoryPlane> > planes;

    for (std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator itNode = mMemPlanes.begin(),
        itNodeEnd = mMemPlanes.end(); itNode != itNodeEnd; ++itNode)
    {
        for (std::vector<MemoryPlane>::const_iterator itPlane
             = (*itNode).second.begin(), itPlaneEnd = (*itNode).second.end();
             itPlane != itPlaneEnd; ++itPlane)
        {
            if ((*itPlane).memSpace == memSpace) {
                std::map<Clock_T, std::vector<MemoryPlane> >::iterator it;
                std::tie(it, std::ignore) = planes.insert(
                    std::make_pair((*itPlane).allocated,
                                   std::vector<MemoryPlane>()));

                (*it).second.push_back((*itPlane));
            }
        }
    }

    // Find the planes allocated at time clock or the one just before
    // => obtain all the planes that are considered valid at the time clock
    Clock_T c = clock;
    std::map<Clock_T, std::vector<MemoryPlane> >::iterator itPlanes;

    do
        itPlanes = planes.find(c);
    while (itPlanes == planes.end() && (c--) > 0);

    assert(itPlanes != planes.end());

    // Fill the stack at time clock
    std::map<unsigned int, unsigned int> stack;

    for (std::vector<MemoryPlane>::const_iterator
        it = (*itPlanes).second.begin(), itEnd = (*itPlanes).second.end();
        it != itEnd; ++it)
    {
        stack.insert(std::make_pair((*it).getContiguousOffset(),
                                    (*it).getContiguousSize()));

        if ((*it).getWrappedSize() > 0) {
            stack.insert(std::make_pair((*it).getWrappedOffset(),
                                        (*it).getWrappedSize()));
        }
    }

    return stack;
}

std::pair<Aidge::MemoryManager::Clock_T, unsigned int>
Aidge::MemoryManager::getMaxHole(std::shared_ptr<MemorySpace> memSpace) const
{
    std::map<Clock_T, unsigned int> holesSize;

    for (std::map<std::shared_ptr<Node>, std::vector<MemoryPlane> >
        ::const_iterator itNode = mMemPlanes.begin(),
        itNodeEnd = mMemPlanes.end(); itNode != itNodeEnd; ++itNode)
    {
        for (std::vector<MemoryPlane>::const_iterator itPlane
             = (*itNode).second.begin(), itPlaneEnd = (*itNode).second.end();
             itPlane != itPlaneEnd; ++itPlane)
        {
            if ((*itPlane).memSpace == memSpace) {
                const unsigned int holeSize = memSpace->size
                    - (*itPlane).getContiguousSize()
                    - (*itPlane).getWrappedSize();

                std::map<Clock_T, unsigned int>::iterator it;
                bool newInsert;
                std::tie(it, newInsert) = holesSize.insert(
                    std::make_pair((*itPlane).allocated, holeSize));

                if (!newInsert) {
                    // Another plane exists at the same time, one must substract
                    // the size of this other plane from the hole size
                    (*it).second = std::max(0, static_cast<int>((*it).second)
                        - static_cast<int>((*itPlane).getContiguousSize())
                        - static_cast<int>((*itPlane).getWrappedSize()));
                }
            }
        }
    }

    return *std::max_element(holesSize.begin(),
                             holesSize.end(),
                             [](const auto& left, const auto& right) {
                                return std::max(left.second, right.second);
                             });
}
