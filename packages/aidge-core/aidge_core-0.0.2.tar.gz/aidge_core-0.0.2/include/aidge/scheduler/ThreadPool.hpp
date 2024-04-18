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

#ifndef AIDGE_CORE_SCHEDULER_THREADPOOL_H_
#define AIDGE_CORE_SCHEDULER_THREADPOOL_H_

#include <thread>
#include <mutex>
#include <queue>
#include <vector>
#include <functional>
#include <condition_variable>
#include <atomic>

namespace Aidge {
class ThreadPool {
public:
    ThreadPool(size_t nbThreads = std::thread::hardware_concurrency());
    void queueJob(const std::function<void()>& job);
    bool busy();
    virtual ~ThreadPool();

private:
    void threadLoop();

    bool mTerminate = false;
    std::mutex mQueueMutex;
    std::condition_variable mMutexCondition;
    std::vector<std::thread> mThreads;
    std::queue<std::function<void()>> mJobs;
};
} // namespace Aidge

#endif /* AIDGE_CORE_SCHEDULER_THREADPOOL_H_ */
