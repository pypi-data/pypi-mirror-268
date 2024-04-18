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

#ifndef AIDGE_CORE_SCHEDULER_MEMORY_MANAGER_H
#define AIDGE_CORE_SCHEDULER_MEMORY_MANAGER_H

#include <memory>
#include <vector>
#include <map>

#include "aidge/graph/Node.hpp"

namespace Aidge {
class MemoryManager {
public:
    typedef int Clock_T;

    enum OptimizeStrategy {
        None,
        OptimizeMaxLifetimeMinSizeFirst,
        OptimizeMaxLifetimeMaxSizeFirst,
        OptimizeMaxHoleMaxLifetimeFirst
    };

    // MemorySpace are contiguous, non-overlapping memory blocks, that can be
    // re-arranged freely.
    struct MemorySpace {
        MemorySpace(Clock_T clock_,
                    unsigned int offset_,
                    unsigned int size_,
                    std::set<std::shared_ptr<Node> > dependencies_
                        = std::set<std::shared_ptr<Node> >()
        ):
            offset(offset_),
            size(size_),
            dependencies(dependencies_),
            allocated(clock_),
            released(-1) {}

        unsigned int offset;
        unsigned int size;
        std::set<std::shared_ptr<Node> > dependencies;
        Clock_T allocated;
        Clock_T released;
    };

    // MemoryPlane belongs to a MemorySpace. Any number of potentially
    // overlapping planes can be associated to a MemorySpace.
    // MemoryPlane can be non-contiguous (in case of stride, or wrapping, when
    // offset + size > memSpace.size).
    // MemoryPlane cannot be re-arranged inside a MemorySpace.
    struct MemoryPlane {
        MemoryPlane(std::shared_ptr<MemorySpace> memSpace_,
                    Clock_T clock_,
                    unsigned int offset_,
                    unsigned int size_,
                    unsigned int stride_ = 0,
                    unsigned int length_ = 1,
                    unsigned int count_ = 1
        ):
            memSpace(memSpace_),
            allocated(clock_),
            offset(offset_),
            size(size_),
            stride(std::max(size_, stride_)),
            length(length_),
            count(count_)
        {
            assert(offset <= memSpace->size);
            // The preceding assert should allow offset == memSpace->size (see
            // issue #63). This means immediate wrapping.
            // It appends if the final offset computed in reallocate() is at
            // the end of the previous memPlane and is also at the end of the
            // memSpace (in case for example of in-place memory op.).
            // Instead of bringing the offset back to the beginning of the
            // memSpace, we stay attached to this offset in case the memSpace
            // grows when a new memPlane is added.

            assert(getContiguousOffset() >= memSpace->offset);
            assert(getWrappedOffset() >= memSpace->offset);
            assert(getContiguousOffset() + getContiguousSize()
                <= memSpace->offset + memSpace->size);
            assert(getWrappedOffset() + getWrappedSize()
                <= memSpace->offset + memSpace->size);
        }

        inline unsigned int getSize() const {
            return stride * length * count;
        }

        inline unsigned int getUsefulSize() const {
            return size * length * count;
        }

        inline unsigned int getContiguousOffset() const {
            return memSpace->offset + offset;
        }

        inline unsigned int getContiguousSize() const {
            return std::min(getSize(), getLimit());
        }

        inline unsigned int getWrappedOffset() const {
            return memSpace->offset;
        }

        inline unsigned int getWrappedSize() const {
            return getSize() - getContiguousSize();
        }

        inline unsigned int getFinalOffset() const {
            return (getWrappedSize() > 0)
                ? getWrappedOffset() + getWrappedSize()
                : getContiguousOffset() + getContiguousSize();
        }

        inline unsigned int getUpperOffset() const {
            return (getContiguousOffset() + getContiguousSize());
        }

        // Limit is computed dynamically, as memSpace->size may increase after
        // the creation of this memory space. This is actually necessary to
        // ensure that the memory wrapping works correctly, because when
        // computing the margin required for the wrapping, it is assumed that
        // the previous layer wrapping extends to the full memory space size.
        inline unsigned int getLimit() const {
            // limit must be a multiple of (stride * length) if count > 1
            // or stride if length > 1
            // uses floor() to stay below memSpace->size
            return (count > 1)
                ? std::floor((memSpace->size - offset)
                        / static_cast<double>(stride * length)) * (stride * length)
                : (length > 1)
                    ? std::floor((memSpace->size - offset)
                            / static_cast<double>(stride)) * stride
                    : memSpace->size - offset;
        }

        std::shared_ptr<MemorySpace> memSpace;
        Clock_T allocated;
        unsigned int offset;
        unsigned int size;
        unsigned int stride;
        unsigned int length;
        unsigned int count;
    };

    struct MaxLifetimeMinSizeFirst {
        MaxLifetimeMinSizeFirst(unsigned int maxLifetime_)
            : maxLifetime(maxLifetime_) {}
        const unsigned int maxLifetime;

        bool operator()(const std::shared_ptr<MemorySpace>& p0,
                        const std::shared_ptr<MemorySpace>& p1);
    };

    struct MaxLifetimeMaxSizeFirst {
        MaxLifetimeMaxSizeFirst(unsigned int maxLifetime_)
            : maxLifetime(maxLifetime_) {}
        const unsigned int maxLifetime;

        bool operator()(const std::shared_ptr<MemorySpace>& p0,
                        const std::shared_ptr<MemorySpace>& p1);
    };

    struct MaxHoleMaxLifetimeFirst {
        MaxHoleMaxLifetimeFirst(unsigned int maxLifetime_, MemoryManager* inst_)
            : maxLifetime(maxLifetime_),
              inst(inst_) {}
        const unsigned int maxLifetime;
        MemoryManager* inst;

        bool operator()(const std::shared_ptr<MemorySpace>& p0,
                        const std::shared_ptr<MemorySpace>& p1);
    };

    struct CompByNodeName {
        bool operator()(const std::shared_ptr<Node>& lhs,
                        const std::shared_ptr<Node>& rhs) const
        {
            return lhs->name() < rhs->name();
        }
    };

    typedef std::map<std::shared_ptr<Node>, std::vector<MemoryPlane>,
        CompByNodeName> MemMap_T;

public:
    MemoryManager(): mClock(0) {}
    ~MemoryManager() noexcept;

public:
    /// Generates a new MemorySpace
    std::shared_ptr<MemorySpace> reserve(unsigned int size,
                                    const std::set<std::shared_ptr<Node> >&
                          dependencies = std::set<std::shared_ptr<Node> >());
    /// Expand an existing MemorySpace, without affecting its MemoryPlane
    /// This function rebuild the memory stack mMemStack
    void expand(std::shared_ptr<MemorySpace> memSpace,
                unsigned int requiredSize);
    /// Generates a MemoryPlane in a new MemorySpace
    MemoryPlane allocate(unsigned int size,
                         const std::set<std::shared_ptr<Node> >&
                          dependencies = std::set<std::shared_ptr<Node> >(),
                         unsigned int stride = 0,
                         unsigned int length = 1,
                         unsigned int count = 1);
    /// Generates a MemoryPlane in a new MemorySpace, associated to a Node
    unsigned int allocate(const std::shared_ptr<Node>& node,
                          unsigned int size,
                          const std::set<std::shared_ptr<Node> >&
                          dependencies = std::set<std::shared_ptr<Node> >(),
                          unsigned int stride = 0,
                          unsigned int length = 1,
                          unsigned int count = 1);
    bool isWrapAround(std::shared_ptr<MemorySpace> memSpace,
                      unsigned int offset,
                      unsigned int size,
                      unsigned int stride = 0,
                      unsigned int length = 1,
                      unsigned int count = 1) const;
    /// Generate a new MemoryPlane in an existing MemorySpace
    MemoryPlane reallocate(std::shared_ptr<MemorySpace> memSpace,
                           unsigned int offset,
                           unsigned int size,
                           bool wrapAround,
                           unsigned int extraSize = 0,
                           const std::set<std::shared_ptr<Node> >&
                additionalDependencies = std::set<std::shared_ptr<Node> >(),
                           unsigned int stride = 0,
                           unsigned int length = 1,
                           unsigned int count = 1);
    /// Generate a new MemoryPlane directly following an existing MemoryPlane
    /// memPlane with an additionnal offset extraOffset
    MemoryPlane reallocate(const MemoryPlane& memPlane,
                           unsigned int extraOffset,
                           unsigned int size,
                           bool wrapAround,
                           unsigned int extraSize = 0,
                           const std::set<std::shared_ptr<Node> >&
                additionalDependencies = std::set<std::shared_ptr<Node> >(),
                           unsigned int stride = 0,
                           unsigned int length = 1,
                           unsigned int count = 1);
    /// Generate a new MemoryPlane in an existing MemorySpace, associated to a
    /// Node
    unsigned int reallocate(std::shared_ptr<MemorySpace> memSpace,
                            const std::shared_ptr<Node>& node,
                            unsigned int offset,
                            unsigned int size,
                            bool wrapAround,
                            unsigned int extraSize = 0,
                            const std::set<std::shared_ptr<Node> >&
                additionalDependencies = std::set<std::shared_ptr<Node> >(),
                            unsigned int stride = 0,
                            unsigned int length = 1,
                            unsigned int count = 1);
    /// Generate a new MemoryPlane directly following an existing MemoryPlane
    /// memPlane with an additionnal offset extraOffset
    unsigned int reallocate(const MemoryPlane& memPlane,
                            const std::shared_ptr<Node>& node,
                            unsigned int extraOffset,
                            unsigned int size,
                            bool wrapAround,
                            unsigned int extraSize = 0,
                            const std::set<std::shared_ptr<Node> >&
                additionalDependencies = std::set<std::shared_ptr<Node> >(),
                            unsigned int stride = 0,
                            unsigned int length = 1,
                            unsigned int count = 1);

    unsigned int release(std::shared_ptr<MemorySpace> memSpace);
    unsigned int release(const std::shared_ptr<Node>& node);
    unsigned int releaseDependencies(const std::shared_ptr<Node>& node);
    void optimize(OptimizeStrategy strategy);
    unsigned int getOffset(const std::shared_ptr<Node>& node,
                           unsigned int plane = 0) const;
    unsigned int getSize(const std::shared_ptr<Node>& node,
                         unsigned int plane) const;
    unsigned int getSize(const std::shared_ptr<Node>& node) const;
    unsigned int getNbPlanes(const std::shared_ptr<Node>& node) const;
    unsigned int getPeakUsage() const;
    Clock_T getMaxLifetime() const;
    const std::vector<MemoryPlane>& getPlanes(const std::shared_ptr<Node>& node)
        const;
    const MemMap_T& getPlanes() const { return mMemPlanes; }
    MemMap_T getPlanes(std::shared_ptr<MemorySpace> memSpace) const;
    unsigned int getNbPlanes(std::shared_ptr<MemorySpace> memSpace) const;
    Clock_T getCurrentTick() const { return mClock; };
    void tick();
    void log(const std::string& fileName) const;

private:
    /// Find a valid offset in the memory stack that can fit a contiguous chunk
    /// of memory of size @size
    unsigned int onStack(unsigned int size);
    unsigned int offStack(unsigned int offset);
    std::map<unsigned int, unsigned int> getStack(
        std::shared_ptr<MemorySpace> memSpace,
        Clock_T clock) const;
    std::pair<Clock_T, unsigned int> getMaxHole(
        std::shared_ptr<MemorySpace> memSpace) const;

    std::map<unsigned int, unsigned int> mMemStack;
    std::vector<std::shared_ptr<MemorySpace> > mMemSpaces;
    MemMap_T mMemPlanes;
    Clock_T mClock;
};
}

namespace {
template <>
const char* const EnumStrings<Aidge::MemoryManager::OptimizeStrategy>::data[]
    = {"None",
       "OptimizeMaxLifetimeMinSizeFirst",
       "OptimizeMaxLifetimeMaxSizeFirst",
       "OptimizeMaxHoleMaxLifetimeFirst"};
}

#endif // AIDGE_CORE_SCHEDULER_MEMORY_MANAGER_H
