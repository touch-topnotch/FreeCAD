#!/bin/bash

set -e
set -x
APP_DIR="../../../build/ARCHI.app"
conda_env="../../../build/ARCHI.app/Contents/Resources"
mkdir -p ${conda_env}

# if [ -d "${APP_DIR}" ]; then
#     rm -rf "${APP_DIR}"
# fi

mkdir -p ${APP_DIR}/Contents/Resources
cp -a ../.pixi/envs/default/* ${conda_env}
# Use rsync to merge directories, preserving existing files
# rsync -a --ignore-existing ${INSTALL_DIR}/ ${conda_env}/

export PATH="${PWD}/${conda_env}/bin:${PATH}"
export CONDA_PREFIX="${PWD}/${conda_env}"

# delete unnecessary stuff
rm -rf ${conda_env}/include
find ${conda_env} -name \*.a -delete
mkdir -p ${conda_env}/bin_tmp
mv ${conda_env}/bin/* ${conda_env}/bin_tmp
mkdir -p ${conda_env}/bin
cp ${conda_env}/bin_tmp/freecad ${conda_env}/bin/
cp ${conda_env}/bin_tmp/freecadcmd ${conda_env}/bin
cp ${conda_env}/bin_tmp/ccx ${conda_env}/bin/
cp ${conda_env}/bin_tmp/python ${conda_env}/bin/
cp ${conda_env}/bin_tmp/pip ${conda_env}/bin/
cp ${conda_env}/bin_tmp/pyside6-rcc ${conda_env}/bin/
cp ${conda_env}/bin_tmp/gmsh ${conda_env}/bin/
cp ${conda_env}/bin_tmp/dot ${conda_env}/bin/
cp ${conda_env}/bin_tmp/unflatten ${conda_env}/bin/
rm -rf ${conda_env}/bin_tmp

sed -i '1s|.*|#!/usr/bin/env python|' ${conda_env}/bin/pip

# copy resources
cp resources/* ${conda_env}

# Remove __pycache__ folders and .pyc files
find . -path "*/__pycache__/*" -delete
find . -name "*.pyc" -type f -delete

# fix problematic rpaths and reexport_dylibs for signing
# see https://github.com/FreeCAD/FreeCAD/issues/10144#issuecomment-1836686775
# and https://github.com/FreeCAD/FreeCAD-Bundle/pull/203
# and https://github.com/FreeCAD/FreeCAD-Bundle/issues/375
python ../scripts/fix_macos_lib_paths.py ${conda_env}/lib

# build and install the launcher

cmake -B build launcher
cmake --build build
mkdir -p ${APP_DIR}/Contents/MacOS
cp build/FreeCAD ${APP_DIR}/Contents/MacOS/ARCHI


python_version=$(python -c 'import platform; print("py" + platform.python_version_tuple()[0] + platform.python_version_tuple()[1])')
version_name="ARCHI_${BUILD_TAG}-macOS-$(uname -m)-${python_version}"
application_menu_name="ARCHI_${BUILD_TAG}"

echo -e "\################"
echo -e "version_name:  ${version_name}"
echo -e "################"

cp Info.plist.template ${conda_env}/../Info.plist
sed -i "s/ARCHI_VERSION/${version_name}/" ${conda_env}/../Info.plist
sed -i "s/APPLICATION_MENU_NAME/${application_menu_name}/" ${conda_env}/../Info.plist

pixi list -e default > ${APP_DIR}/Contents/packages.txt
sed -i '1s/.*/\nLIST OF PACKAGES:/' ${APP_DIR}/Contents/packages.txt

# copy the plugin into its final location
if [ -d "${conda_env}/Library" ]; then
    cp -a ${conda_env}/Library ${conda_env}/..
    rm -rf ${conda_env}/Library
else
    echo "Warning: Library directory not found in ${conda_env}"
fi

if [[ "${SIGN_RELEASE}" == "true" ]]; then
    # create the signed dmg
    ./macos_sign_and_notarize.zsh -p "ARCHI" -k ${SIGNING_KEY_ID} -o "../../../build/bundle/${version_name}.dmg"
else
    # create the dmg
    dmgbuild -s dmg_settings.py "ARCHI" "../../../build/bundle/${version_name}.dmg"
fi

# create hash
sha256sum "../../../build/bundle/${version_name}.dmg" > "../../../build/bundle/${version_name}.dmg-SHA256.txt"

if [[ "${UPLOAD_RELEASE}" == "true" ]]; then
    gh release upload --clobber ${BUILD_TAG} "../../../build/bundle/${version_name}.dmg" "../../../build/bundle/${version_name}.dmg-SHA256.txt"
fi