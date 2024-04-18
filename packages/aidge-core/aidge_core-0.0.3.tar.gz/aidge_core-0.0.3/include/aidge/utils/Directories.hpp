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


#ifndef AIDGE_DIRECTORIES_H_
#define AIDGE_DIRECTORIES_H_


#include <string>  // std::string
#include <sstream> // std::stringstream
#include <iostream>
#include <sys/stat.h>
#include <errno.h>

#ifdef WIN32
#include <direct.h>
#else
#include <sys/types.h>
#include <unistd.h>
#endif

namespace Aidge {

    bool isNotValidFilePath(int c) {
        return (iscntrl(c)
            || c == '<'
            || c == '>'
            || c == ':'
            || c == '"'
            || c == '|'
            || c == '?'
            || c == '*');
    }

    std::string filePath(const std::string& str) {
        std::string filePath(str);
        std::replace_if(filePath.begin(), filePath.end(),
                        isNotValidFilePath, '_');
        return filePath;
    }


    bool createDirectories(const std::string& dirName)
    {
        std::stringstream path(dirName);
        std::string dir;
        std::string pathToDir("");
        int status = 0;

        while (std::getline(path, dir, '/') && status == 0) {
            pathToDir += dir + '/';
            struct stat fileStat;
            if (stat(pathToDir.c_str(), &fileStat) != 0) {
                // Directory does not exist
    #ifdef WIN32
                status = _mkdir(pathToDir.c_str());
    #else
    #if defined(S_IRWXU)
                status = mkdir(pathToDir.c_str(), S_IRWXU | S_IRWXG | S_IRWXO);
    #else
                status = mkdir(pathToDir.c_str());
    #endif
    #endif
            } else if (!S_ISDIR(fileStat.st_mode)) {
                status = -1;
            }
        }
        return (status == 0 || errno == EEXIST);
    }


}

#endif //AIDGE_DIRECTORIES_H_

