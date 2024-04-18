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

#include "aidge/utils/Log.hpp"
#include "aidge/utils/ErrorHandling.hpp"

#include <cstdlib>

#include <fmt/color.h>
#include <fmt/chrono.h>

Aidge::Log::Level Aidge::Log::mConsoleLevel = []() {
    const char* logLevel = std::getenv("AIDGE_LOGLEVEL_CONSOLE");
    if (logLevel != nullptr) {
        for (std::size_t i = 0; i < size(EnumStrings<Log::Level>::data); ++i) {
            if (std::string(logLevel) == EnumStrings<Log::Level>::data[i]) {
                return static_cast<Log::Level>(i);
            }
        }
    }
    return Info;
}();
Aidge::Log::Level Aidge::Log::mFileLevel = []() {
    const char* logLevel = std::getenv("AIDGE_LOGLEVEL_FILE");
    if (logLevel != nullptr) {
        for (std::size_t i = 0; i < size(EnumStrings<Log::Level>::data); ++i) {
            if (std::string(logLevel) == EnumStrings<Log::Level>::data[i]) {
                return static_cast<Log::Level>(i);
            }
        }
    }
    return Debug;
}();
std::string Aidge::Log::mFileName = []() {
    const char* logFile = std::getenv("AIDGE_LOG_FILE");
    if (logFile != nullptr) {
        return std::string(logFile);
    }
    return std::string();
}();
std::unique_ptr<FILE, decltype(&std::fclose)> Aidge::Log::mFile {nullptr, nullptr};
std::vector<std::string> Aidge::Log::mContext;

void Aidge::Log::log(Level level, const std::string& msg) {
    if (level >= mConsoleLevel) {
        // Apply log level style only for console.
        // Styles that were already applied to msg with fmt are kept also in 
        // the log file.
        const auto modifier
            = (level == Debug) ? fmt::fg(fmt::color::gray)
            : (level == Notice) ? fmt::fg(fmt::color::light_yellow)
            : (level == Warn) ? fmt::fg(fmt::color::orange)
            : (level == Error) ? fmt::fg(fmt::color::red)
            : (level == Fatal) ? fmt::bg(fmt::color::red)
            : fmt::text_style();

        for (const auto& context : mContext) {
            fmt::println("Context: {}", context);
        }

        fmt::println("{}", fmt::styled(msg, modifier));
    }

    if (level >= mFileLevel && !mFileName.empty()) {
        if (!mFile) {
            initFile(mFileName);
        }

        for (const auto& context : mContext) {
            fmt::println("Context: {}", context);
        }

        fmt::println(mFile.get(), msg);
    }
}

void Aidge::Log::initFile(const std::string& fileName) {
    mFile = std::unique_ptr<FILE, decltype(&std::fclose)>(std::fopen(fileName.c_str(), "a"), &std::fclose);

    if (!mFile) {
        mFileName.clear(); // prevents AIDGE_THROW_OR_ABORT() to try to log into file
        AIDGE_THROW_OR_ABORT(std::runtime_error,
            "Could not create log file: {}", fileName);
    }

    const std::time_t t = std::time(nullptr);
    fmt::println(mFile.get(), "###### {:%Y-%m-%d %H:%M:%S} ######", fmt::localtime(t));
}
