:: create the conda environment as a subdirectory
call mamba env create -p .conda/freecad -f conda/conda-env-qt6.yaml

:: add the environment subdirectory to the conda configuration
call conda config --add envs_dirs %CONDA_PREFIX%/envs
call conda config --add envs_dirs %CD%/.conda
call conda config --set env_prompt "({name})"

:: install the FreeCAD dependencies into the environment 
:: if KeyError: 'envs_dirs' happens, just ignore it and execute  mamba env update -n freecad -f conda/environment-qt6.yml
call mamba run -n freecad mamba-devenv --no-prune -f conda/environment-qt6.devenv.yml
call mamba env update -n freecad -f conda/environment-qt6.yml


:: install clang_win-64 compiler specifically for the local environment
call mamba install -p .conda/freecad -c conda-forge clang_win-64
