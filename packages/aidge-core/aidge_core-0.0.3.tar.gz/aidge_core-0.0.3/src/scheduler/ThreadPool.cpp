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

#include "aidge/scheduler/ThreadPool.hpp"

Aidge::ThreadPool::ThreadPool(size_t nbThreads) {
    for (size_t i = 0; i < nbThreads; ++i) {
        mThreads.emplace_back(std::thread(&ThreadPool::threadLoop, this));
    }
}

void Aidge::ThreadPool::threadLoop() {
    while (true) {
        std::function<void()> job;
        {
            std::unique_lock<std::mutex> lock(mQueueMutex);
            mMutexCondition.wait(lock, [this] {
                return !mJobs.empty() || mTerminate;
            });
            if (mTerminate) {
                return;
            }
            job = mJobs.front();
            mJobs.pop();
        }
        job();
    }
}

void Aidge::ThreadPool::queueJob(const std::function<void()>& job) {
    {
        std::unique_lock<std::mutex> lock(mQueueMutex);
        mJobs.push(job);
    }
    mMutexCondition.notify_one();
}

bool Aidge::ThreadPool::busy() {
    bool poolbusy;
    {
        std::unique_lock<std::mutex> lock(mQueueMutex);
        poolbusy = !mJobs.empty();
    }
    return poolbusy;
}

Aidge::ThreadPool::~ThreadPool() {
    {
        std::unique_lock<std::mutex> lock(mQueueMutex);
        mTerminate = true;
    }
    mMutexCondition.notify_all();
    for (std::thread& active_thread : mThreads) {
        active_thread.join();
    }
    mThreads.clear();
}
