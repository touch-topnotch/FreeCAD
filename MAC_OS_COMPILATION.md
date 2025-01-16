# Compilation for macOS

This guide outlines the steps to build FreeCAD from `HEAD` using `mamba`/`conda`.

## Prerequisites

1. Install [mambaforge](https://github.com/mamba-org/mamba) (a C++ implementation of conda).
```bash
% brew install mambaforge
```
Note: If you have miniforge installed, you must remove it first:
```bash
% brew remove miniforge
% brew install mambaforge
```
2.	Remove boost and any Homebrew formulas that depend on it, if installed. To find dependencies:

```bash
% brew info boost
% brew uses --recursive --installed boost
```
Note: While boost must be removed, libspnav is required for the build to succeed.

3.	Install libspnav using Homebrew if not already installed:
```bash
% brew info libspnav
% brew install libspnav
```
Building FreeCAD with mamba/conda

1. Initialize mamba/conda and Update Shell Configuration
```bash
% conda init "$(basename "${SHELL}")"
% source ~/.zshrc
```
2. Clone FreeCAD and Its Submodules
```bash
% git clone --recurse-submodules git@github.com:touch-topnotch/FreeCAD.git FreeCAD
% cd FreeCAD
```
3. Check the Current Commit

This step is useful for reporting issues later:
```bash
main % git log -1 --format=medium
```

Example output:
```bash
commit de9be04249c862891d2a6903b5661460452796c7 (HEAD -> main, origin/main, origin/HEAD)
Merge: 36a7fd9be4 e3648061fd
Author: Chris Hennes <chennes@pioneerlibrarysystem.org>
Date:   Tue Jun 4 19:15:12 2024 -0500

    Merge pull request #14491 from marioalexis84/fem-test_file_license
    Fem: Set compatible license in test files - fixes #8894
```

4. Set Up Conda/Mamba Environment for FreeCAD
```bash
main % source ./conda/setup-environment.sh
main % conda activate freecad
```
5. Confirm the Correct cmake is Being Used

Set the PATH to the cmake binary in the FreeCAD conda environment.
```bash
(freecad)FreeCAD main % export PATH=/path/to/FreeCAD/.conda/freecad/bin:$PATH
```

Ensure the correct cmake binary is being used:
```bash
(freecad)FreeCAD main % which cmake
/path/to/FreeCAD/.conda/freecad/bin/cmake
```

6. List Available CMake Presets
```bash
(freecad)FreeCAD main % cmake --list-presets
```
Example output:
```bash
Available configure presets:
  "debug"               - Debug
  "release"             - Release
  "conda-macos-debug"   - Conda Debug
  "conda-macos-release" - Conda Release
```
7. Generate Build Configuration for the “conda-macos-release” Preset
```bash
(freecad)FreeCAD main % cmake --preset conda-macos-release
```
8. (Optional) Clean Build Targets
```bash
(freecad)FreeCAD main % cmake --build ./build/release --parallel 12 --target clean
```
9. Build FreeCAD
```bash
(freecad)FreeCAD main % cmake --build ./build/release --parallel 12
```
If the build completes without errors, you can start FreeCAD from the shell to view additional options:
```bash
% ./build/release/bin/FreeCAD --help
```
Alternatively, launch FreeCAD as a regular application:
```bash
% ./build/release/bin/FreeCAD
```
This process ensures FreeCAD is built successfully on macOS using the mamba/conda toolchain. For additional help or troubleshooting, refer to the FreeCAD documentation.

