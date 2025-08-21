# shapecomp

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/pgroenbaek/shapecomp?style=flat&label=Latest%20Version)](https://github.com/pgroenbaek/shapecomp/releases)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License GNU GPL v3](https://img.shields.io/badge/License-%20%20GNU%20GPL%20v3%20-lightgrey?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgNTEyIj4KICA8IS0tIEZvbnQgQXdlc29tZSBGcmVlIDYuNy4yIGJ5IEBmb250YXdlc29tZSAtIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tIExpY2Vuc2UgLSBodHRwczovL2ZvbnRhd2Vzb21lLmNvbS9saWNlbnNlL2ZyZWUgQ29weXJpZ2h0IDIwMjUgRm9udGljb25zLCBJbmMuIC0tPgogIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNMzg0IDMybDEyOCAwYzE3LjcgMCAzMiAxNC4zIDMyIDMycy0xNC4zIDMyLTMyIDMyTDM5OC40IDk2Yy01LjIgMjUuOC0yMi45IDQ3LjEtNDYuNCA1Ny4zTDM1MiA0NDhsMTYwIDBjMTcuNyAwIDMyIDE0LjMgMzIgMzJzLTE0LjMgMzItMzIgMzJsLTE5MiAwLTE5MiAwYy0xNy43IDAtMzItMTQuMy0zMi0zMnMxNC4zLTMyIDMyLTMybDE2MCAwIDAtMjk0LjdjLTIzLjUtMTAuMy00MS4yLTMxLjYtNDYuNC01Ny4zTDEyOCA5NmMtMTcuNyAwLTMyLTE0LjMtMzItMzJzMTQuMy0zMiAzMi0zMmwxMjggMGMxNC42LTE5LjQgMzcuOC0zMiA2NC0zMnM0OS40IDEyLjYgNjQgMzJ6bTU1LjYgMjg4bDE0NC45IDBMNTEyIDE5NS44IDQzOS42IDMyMHpNNTEyIDQxNmMtNjIuOSAwLTExNS4yLTM0LTEyNi03OC45Yy0yLjYtMTEgMS0yMi4zIDYuNy0zMi4xbDk1LjItMTYzLjJjNS04LjYgMTQuMi0xMy44IDI0LjEtMTMuOHMxOS4xIDUuMyAyNC4xIDEzLjhsOTUuMiAxNjMuMmM1LjcgOS44IDkuMyAyMS4xIDYuNyAzMi4xQzYyNy4yIDM4MiA1NzQuOSA0MTYgNTEyIDQxNnpNMTI2LjggMTk1LjhMNTQuNCAzMjBsMTQ0LjkgMEwxMjYuOCAxOTUuOHpNLjkgMzM3LjFjLTIuNi0xMSAxLTIyLjMgNi43LTMyLjFsOTUuMi0xNjMuMmM1LTguNiAxNC4yLTEzLjggMjQuMS0xMy44czE5LjEgNS4zIDI0LjEgMTMuOGw5NS4yIDE2My4yYzUuNyA5LjggOS4zIDIxLjEgNi43IDMyLjFDMjQyIDM4MiAxODkuNyA0MTYgMTI2LjggNDE2UzExLjcgMzgyIC45IDMzNy4xeiIvPgo8L3N2Zz4=&logoColor=%23ffffff)](/LICENSE)

> 🚧 **Project Status: In Development**  
> This project is not feature-complete and is still being actively developed.  
> Expect missing functionality, incomplete features, and frequent changes.

This Python module provides functions for compressing and decompressing shape files.

Unlike other tools for compressing and decompressing shapes this Python module also works on Linux and macOS. It is powered by the `TK.MSTS.Tokens.dll` library from Okrasa Ghia.

List of companion modules:
- [shapeio](https://github.com/pgroenbaek/shapeio) - offers functions to convert shapes between structured text format and Python objects.
- [shapeedit](https://github.com/pgroenbaek/shapeedit) - provides a wrapper for modifying the shape data structure safely.
- [trackshape-utils](https://github.com/pgroenbaek/trackshape-utils/tree/develop) - offers additional utilities for working with track shapes.


## Prerequisites

This module uses the `TK.MSTS.Tokens.dll` library by Okrasa Ghia to perform shape file compression and decompression. Therefore, a Common Language Runtime (CLR) is required if you wish to compress and decompress shapes programmatically through the module. You can use the Mono runtime on Linux and macOS, or the .NET Framework on Windows.

The `TK.MSTS.Tokens.dll` library is not included with the Python module. It can be downloaded as part of the TK\_Utils package from [the-train.de](https://the-train.de/downloads/entry/9385-tk-utils-updated/). Only the DLL file itself is needed from that package.

See the [Usage section](#usage) for more details on how to compress and decompress shape files using the module.

Steps to install a CLR on your operating system:

#### Linux

```bash
sudo apt update
sudo apt install mono-complete
```

#### macOS

```bash
brew install mono
```

#### Windows

Download and install the [.NET Framework 4.0 or later](https://dotnet.microsoft.com/en-us/download/dotnet-framework) from Microsoft.

The .NET Framework is typically already installed on most Windows systems.


## Installation

<!-- ### Install from PyPI

```sh
pip install --upgrade shapeedit
```

### Install from wheel

If you have downloaded a `.whl` file from the [Releases](https://github.com/pgroenbaek/shapeedit/releases) page, install it with:

```sh
pip install path/to/shapeedit-<version>‑py3‑none‑any.whl
```

Replace `<version>` with the actual version number in the filename. For example:

```sh
pip install path/to/shapeedit-0.5.0b0-py3-none-any.whl
``` -->

### Install from source

```sh
git clone https://github.com/pgroenbaek/shapecomp.git
pip install --upgrade ./shapecomp
```

## Usage

### Check if a shape is compressed on disk

To check whether a shape file on disk is compressed, you can use the `is_compressed` function. This function returns `True` if the shape is compressed and `False` if it is not. If the file is empty, not a shape file, or its state cannot be determined, the function will return `None`.

```python
import shapecomp as sc

is_comp = sc.is_compressed("./path/to/example.s")
if is_comp is True:
    print("Compressed")
elif is_comp is False:
    print("Uncompressed")
else:
    print("Could not determine (possibly empty file)")
```

### Compress or decompress a shape on disk

The compression and decompression functions in this module use the `TK.MSTS.Tokens.dll` library by Okrasa Ghia. This library is not included with the Python module. You will also need a CLR installed to load this file.

See the [Prerequisites section](#prerequisites) for instructions on how to obtain the `TK.MSTS.Tokens.dll` library and set up a CLR on your operating system.

Alternatively, you can manually compress and decompress shapes using other tools, such as *ffeditc\_unicode.exe* through the [Shape File Manager](https://www.trainsim.com/forums/filelib-search-fileid?fid=78928) or the [FFEDIT\_Sub v1.2](https://www.trainsim.com/forums/filelib-search-fileid?fid=40291) utility by Ged Saunders.

```python
import shapecomp as sc

dll_path = "./path/to/TK.MSTS.Tokens.dll"

# Compress and decompress in-place.
sc.compress(dll_path, "./path/to/example.s")
sc.decompress(dll_path, "./path/to/example.s")

# Compress and decompress to an output file.
sc.compress(dll_path, "./path/to/example.s", "./path/to/output.s")
sc.decompress(dll_path, "./path/to/example.s", "./path/to/output.s")
```


## Running Tests

You can run tests manually or use `tox` to test across multiple Python versions.

### Run Tests Manually
First, install the required dependencies:

```sh
pip install pytest
```

Then, run tests with:

```sh
pytest
```


## Run Tests with `tox`

`tox` allows you to test across multiple Python environments.

### **1. Install `tox`**
```sh
pip install tox
```

### **2. Run Tests**
```sh
tox
```

This will execute tests in all specified Python versions.

### **3. `tox.ini` Configuration**
The `tox.ini` file should be in your project root:

```ini
[tox]
envlist = py36, py37, py38, py39, py310

[testenv]
deps = pytest
commands = pytest
```

Modify `envlist` to match the Python versions you want to support.

## License

This Python module was created by Peter Grønbæk Andersen and is licensed under [GNU GPL v3](/LICENSE).
