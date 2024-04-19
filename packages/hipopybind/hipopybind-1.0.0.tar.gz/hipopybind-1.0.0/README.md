#  HipopyBind : HIPO PyBind11 Library

## Prerequisites

* Python >=3.7.3
* A compiler with C++11 support
* Pip 10+ or CMake >= 3.4 (or 3.14+ on Windows, which was the first version to support VS 2019)
* Ninja or Pip 10+

## Installation

To install from PyPi run:

```bash
pip install hipopybind
```

To compile the library from source run the following:

```bash
git clone --recurse-submodules https://github.com/mfmceneaney/hipopybind.git
cd hipopybind
cmake .
make
```

And add the following to your startup script:

```bash
export PYTHONPATH=$PYTHONPATH\:/path/to/hipopybind
```

# Developer Note
For updating submodules run the following:

```bash
git submodule update --init --recursive
```

#

Contact: matthew.mceneaney@duke.edu
