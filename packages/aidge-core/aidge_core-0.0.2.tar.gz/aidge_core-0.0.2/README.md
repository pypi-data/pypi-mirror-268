![Pipeline status](https://gitlab.eclipse.org/eclipse/aidge/aidge_core/badges/main/pipeline.svg?ignore_skipped=true) ![C++ coverage](https://gitlab.eclipse.org/eclipse/aidge/aidge_core/badges/main/coverage.svg?job=coverage:ubuntu_cpp&key_text=C%2B%2B+coverage&key_width=90) ![Python coverage](https://gitlab.eclipse.org/eclipse/aidge/aidge_core/badges/main/coverage.svg?job=coverage:ubuntu_python&key_text=Python+coverage&key_width=100)

# Aidge Core library

You can find here the C++ code of the Core library of Aidge.

## Pip installation



To install aidge_core using pip, run the following command in your python environnement :
``` bash
pip install . -v
```

**Note:** you can specify a custom install folder by setting an environment variable:

``` bash
export AIDGE_INSTALL='<path_to_aidge>/install'
```

## Standard C++ Compilation

Create two directories ``build`` and ``ìnstall``.

Then **inside** ``build`` :

```bash

cmake -DCMAKE_INSTALL_PREFIX:PATH=$(path_to_install_folder) $(CMAKE PARAMETERS) $(projet_root)

make all install

```


**Compilation options**


|   Option   | Value type | Description |
|:----------:|:----------:|:-----------:|
| *-DCMAKE_INSTALL_PREFIX:PATH* | ``str``  | Path to the install folder |
| *-DCMAKE_BUILD_TYPE*          | ``str``  | If ``Debug``, compile in debug mode, ``Release`` compile with highest optimisations, default= ``Release`` |
| *-DWERROR*                    | ``bool`` | If ``ON`` show warning as error during compilation phase, default=``OFF`` |
| *-DPYBIND*                    | ``bool`` | If ``ON`` activate python binding, default=``ON`` |

If you have compiled with PyBind you can find at the root of the ``build`` file the python lib ``aidge_core.cpython*.so``

## Run tests

### CPP

Inside of the build file run:

```bash

ctest --output-on-failure

```

### Python

