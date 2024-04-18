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


#ifndef AIDGE_LOG_H_
#define AIDGE_LOG_H_

#include <memory>

#include <fmt/format.h>
#include <fmt/ranges.h>

#include "aidge/utils/Attributes.hpp"

namespace Aidge {
/**
 * Helper to define a context anywhere, hidding the scoped variable name
 * which has no relevance.
*/
#define AIDGE_LOG_CONTEXT(...) const Log::Context logContext_##__LINE__(__VA_ARGS__)


template<class U>
static void discard_args(U parg) {
    (void)parg;
}
template<class U, class... Us>
static void discard_args(U parg, Us... pargs) {
    (void)parg;
    discard_args(pargs...);
}

/**
 * Aidge logging class, for displaying and file logging of events.
*/
class Log {
public:
    enum Level {
        Debug = 0,
        Info,
        Notice,
        Warn,
        Error,
        Fatal
    };

    class Context {
    public:
        template <typename... Args>
        Context(Args&&... args) {
            Log::mContext.push_back(fmt::format(std::forward<Args>(args)...));
        }

        ~Context() {
            Log::mContext.pop_back();
        }
    };

    /**
     * Detailed messages for debugging purposes, providing information helpful
     * for developers to trace and identify issues.
     * Detailed insights of what is appening in an operation, not useful for the
     * end-user. The operation is performed nominally.
     * @note This level is disabled at compile time for Release, therefore
     * inducing no runtime overhead for Release.
    */
    template <typename... Args>
    constexpr static void debug(Args&&... args) {
#ifndef NDEBUG
        // only when compiled in Debug
        log(Debug, fmt::format(std::forward<Args>(args)...));
#else
        discard_args(&args...);
#endif
    }

    /**
     * Messages that provide a record of the normal operation, about
     * the application's state, progress, or important events.
     * Reports normal start, end and key steps in an operation. The operation is
     * performed nominally.
    */
    template <typename... Args>
    constexpr static void info(Args&&... args) {
        log(Info, fmt::format(std::forward<Args>(args)...));
    }

    /**
     * Applies to normal but significant conditions that may require monitoring,
     * like unusual or normal fallback events.
     * Reports specific paths in an operation. The operation can still be
     * performed normally.
    */
    template <typename... Args>
    constexpr static void notice(Args&&... args) {
        log(Notice, fmt::format(std::forward<Args>(args)...));
    }

    /**
     * Indicates potential issues or situations that may lead to errors but do
     * not necessarily cause immediate problems.
     * Some specific steps of the operation could not be performed, but it can
     * still provide an exploitable result.
    */
    template <typename... Args>
    constexpr static void warn(Args&&... args) {
        log(Warn, fmt::format(std::forward<Args>(args)...));
    }

    /**
     * Signifies a problem or unexpected condition that the application can
     * recover from, but attention is needed to prevent further issues.
     * The operation could not be performed, but it does not prevent potential
     * further operations.
    */
    template <typename... Args>
    constexpr static void error(Args&&... args) {
        log(Error, fmt::format(std::forward<Args>(args)...));
    }

    /**
     * Represents a critical error or condition that leads to the termination of
     * the application, indicating a severe and unrecoverable problem.
     * The operation could not be performed and any further operation is
     * impossible.
    */
    template <typename... Args>
    constexpr static void fatal(Args&&... args) {
        log(Fatal, fmt::format(std::forward<Args>(args)...));
    }

    /**
     * Set the minimum log level displayed in the console.
    */
    constexpr static void setConsoleLevel(Level level) {
        mConsoleLevel = level;
    }

    /**
     * Set the minimum log level saved in the log file.
    */
    constexpr static void setFileLevel(Level level) {
        mFileLevel = level;
    }

    /**
     * Set the log file name.
     * Close the current log file and open the one with the new file name.
     * If empty, stop logging into a file.
    */
    static void setFileName(const std::string& fileName) {
        if (fileName != mFileName) {
            mFileName = fileName;
            mFile.release();

            if (!fileName.empty()) {
                initFile(fileName);
            }
        }
    }

private:
    static void log(Level level, const std::string& msg);
    static void initFile(const std::string& fileName);

    static Level mConsoleLevel;
    static Level mFileLevel;
    static std::string mFileName;
    static std::unique_ptr<FILE, decltype(&std::fclose)> mFile;
    static std::vector<std::string> mContext;
};
}

namespace {
template <>
const char *const EnumStrings<Aidge::Log::Level>::data[] = {"Debug", "Info", "Notice", "Warn", "Error", "Fatal"};
}

#endif //AIDGE_LOG_H_
