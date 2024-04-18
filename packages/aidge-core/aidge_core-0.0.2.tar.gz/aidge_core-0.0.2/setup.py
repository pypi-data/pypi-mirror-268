#!/usr/bin/env python3
""" Aidge

#TODO To change
POC of the next framework named Aidge
"""

DOCLINES = (__doc__ or '').split("\n")

import sys
import os

# Python supported version checks
if sys.version_info[:2] < (3, 7):
    raise RuntimeError("Python version >= 3.7 required.")


CLASSIFIERS = """\
Development Status :: 2 - Pre-Alpha
"""

import shutil
import pathlib
import subprocess
import multiprocessing

from math import ceil

from setuptools import setup, Extension
from setuptools import find_packages
from setuptools.command.build_ext import build_ext

def get_project_name() -> str:
    return open(pathlib.Path().absolute() / "project_name.txt", "r").read()

def get_project_version() -> str:
    aidge_root = pathlib.Path().absolute()
    version = open(aidge_root / "version.txt", "r").read().strip()
    return version


class CMakeExtension(Extension):
    def __init__(self, name):
        super().__init__(name, sources=[])

class CMakeBuild(build_ext):

    def run(self):
        # This lists the number of processors available on the machine
        # The compilation will use half of them
        max_jobs = str(ceil(multiprocessing.cpu_count() / 2))

        cwd = pathlib.Path().absolute()

        build_temp = cwd / "build_aidge"
        if not build_temp.exists():
            build_temp.mkdir(parents=True, exist_ok=True)

        build_lib = pathlib.Path(self.build_lib)
        if not build_lib.exists():
            build_lib.mkdir(parents=True, exist_ok=True)

        aidge_package = build_lib / (get_project_name())

        self.spawn([f"ls", f"{str(aidge_package.absolute())}"])

        self.spawn([f"ls", f"{str(build_temp.absolute())}"])

        os.chdir(str(build_temp))

        # Impose to use the executable of the python
        # used to launch setup.py to setup PythonInterp
        param_py = "-DPYTHON_EXECUTABLE=" + sys.executable

        self.spawn([f"{sys.executable}", "--version"])
        print(sys.executable, " --version")

        compile_type = 'Debug'
        # install_path = os.path.join(sys.prefix, "lib", "libAidge")  if "AIDGE_INSTALL" not in os.environ else os.environ["AIDGE_INSTALL"]
        # install_path = str((aidge_package / "lib").absolute())
        install_path = str(build_temp.absolute() / "libAidge")

        self.spawn(['cmake', str(cwd), param_py, '-DTEST=OFF', f'-DCMAKE_INSTALL_PREFIX:PATH={install_path}', f'-DCMAKE_BUILD_TYPE={compile_type}'])
        if not self.dry_run:
            self.spawn(['cmake', '--build', '.', '--config', compile_type, '-j', max_jobs])
            self.spawn(['cmake', '--install', '.', '--config', compile_type])
        
        os.chdir(str(cwd))

        # Get "aidge core" package
        # ext_lib = build_temp
        self.spawn([f"ls", f"-R", f"{str(build_temp.absolute())}"])
        self.spawn([f"ls", f"-R", f"{str(install_path)}"])
        self.spawn([f"ls", f"-R", f"{str(aidge_package.absolute())}"])
        # Copy all shared object files from build_temp/lib to aidge_package
        for root, folders, files in os.walk(build_temp.absolute()):
            for file in files:
                # if (file.endswith('.pyd')) and (root != str(aidge_package.absolute())):
                if (file.endswith('.so') or file.endswith('.pyd') or file.endswith('.cmake')) and (root != str(aidge_package.absolute())):
                    currentFile=os.path.join(root, file)
                    shutil.copy(currentFile, str(aidge_package.absolute()))


        self.spawn([f"ls", f"{str(aidge_package.absolute())}"])

        lib_temp = build_temp / "libAidge"
        # Copy lib folder
        for root, folders, files in os.walk(lib_temp.absolute()):
            for folder in folders:
                if (folder.endswith('include')):
                    currentFolder=os.path.join(root, folder)
                    self.spawn([f"ls", f"{str(currentFolder)}"])
                    shutil.copytree(currentFolder, str(aidge_package.absolute()), dirs_exist_ok=True)

        libfmt_temp = build_temp / "libAidge" / "lib"
        # Copy libfmtd.a lib
        for root, folders, files in os.walk(libfmt_temp.absolute()):
            for file in files:
                # if (file.endswith('.pyd')) and (root != str(aidge_package.absolute())):
                if (file.endswith('libfmtd.a')) and (root != str(aidge_package.absolute())):
                    currentFile=os.path.join(root, file)
                    shutil.copy(currentFile, str(aidge_package.absolute()))

        self.spawn([f"ls", f"-R", f"{str(aidge_package.absolute())}"])

        # Copy version.txt in aidge_package
        os.chdir(os.path.dirname(__file__))
        shutil.copy("version.txt", str(aidge_package.absolute()))
        shutil.copy("project_name.txt", str(aidge_package.absolute())) 

        self.spawn([f"ls", f"-R", f"{str(aidge_package.absolute())}"])


if __name__ == '__main__':

    setup(
        name=get_project_name(),
        version=get_project_version(),
        python_requires='>=3.7',
        description=DOCLINES[0],
        long_description_content_type="text/markdown",
        long_description="\n".join(DOCLINES[2:]),
        classifiers=[c for c in CLASSIFIERS.split('\n') if c],
        packages=find_packages(where="."),
        include_package_data=True,
        ext_modules=[CMakeExtension(get_project_name())],
        cmdclass={
            'build_ext': CMakeBuild,
        },
        zip_safe=False,

    )
