#!/bin/sh

# Check if the script is being run from the 'freecad' environment
if [ "$CONDA_DEFAULT_ENV" != "freecad" ]; then
	echo "Activating the 'freecad' environment..."
	conda activate freecad
fi

# Create the conda environment as a subdirectory if it doesn't already exist
if [ ! -d ".conda/freecad" ]; then
	mamba env create -p .conda/freecad -f conda/conda-env-qt6.yaml
else
	echo "Conda environment 'freecad' already exists. Skipping creation."
fi

# Add the environment subdirectory to the conda configuration
conda config --add envs_dirs $CONDA_PREFIX/envs
conda config --add envs_dirs $(pwd)/.conda

# Run mamba-devenv to install dependencies
conda config --set env_prompt "({name})"

# Install the FreeCAD dependencies into the environment
mamba run --live-stream -n freecad mamba-devenv --no-prune -f conda/environment-qt6.devenv.yml
# Uninstall qt-main from the 'freecad' environment
conda uninstall qt-main