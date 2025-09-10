# !/bin/bash

set -e
set -x

conda_env="ARCHI.app/Contents/Resources"

mkdir -p ${conda_env}

# if [ -d "${APP_DIR}" ]; then
#     rm -rf "${APP_DIR}"
# fi

mkdir -p ${APP_DIR}/Contents/Resources
cp -a ../.pixi/envs/default/* ${conda_env}
# Use rsync to merge directories, preserving existing files
# rsync -a --ignore-existing ${INSTALL_DIR}/ ${conda_env}/

# Overlay repo Python modules to ensure latest sources are bundled (overrides env copies)
if [[ -d ../../../src/Mod ]]; then
    mkdir -p ${conda_env}/Mod
    cp -a ../../../src/Mod/* ${conda_env}/Mod/ 2>/dev/null || true
fi

# Ensure all auxiliary Python modules (Ext) are available in the bundle
# Merge from multiple known locations without special-casing per module.
mkdir -p ${conda_env}/Ext

# 1) Copy any Ext content produced by the main build
if [[ -d ../../../build/release/Ext ]]; then
    cp -a ../../../build/release/Ext/* ${conda_env}/Ext/ 2>/dev/null || true
fi

# 2) Copy any Ext content produced by pixi build helpers (e.g., PySide shims)
if [[ -d ../.pixi/build/Ext ]]; then
    cp -a ../.pixi/build/Ext/* ${conda_env}/Ext/ 2>/dev/null || true
fi

# 3) Fallback: copy pure-Python third-party modules from source tree into Ext if missing
if [[ -d ../../../src/3rdParty ]]; then
    for pkg in ../../../src/3rdParty/*; do
        base_name=$(basename "$pkg")
        # Skip non-directories and CMakeLists etc.
        [[ -d "$pkg" ]] || continue
        [[ -e "$pkg/CMakeLists.txt" ]] || true
        # Only copy if it looks like a Python package/module and not already present in Ext
        if [[ ! -e ${conda_env}/Ext/${base_name} ]]; then
            if ls "$pkg"/*.py >/dev/null 2>&1 || [[ -f "$pkg/__init__.py" ]]; then
                mkdir -p ${conda_env}/Ext/${base_name}
                cp -a "$pkg"/*.py ${conda_env}/Ext/${base_name}/ 2>/dev/null || true
                [[ -f "$pkg/__init__.py" ]] && cp -a "$pkg/__init__.py" ${conda_env}/Ext/${base_name}/ 2>/dev/null || true
            fi
        fi
    done
fi


# Overlay repo Python modules to ensure latest sources are bundled (overrides env copies)
if [[ -d ../../../src/Mod ]]; then
    mkdir -p ${conda_env}/Mod
    cp -a ../../../src/Mod/* ${conda_env}/Mod/ 2>/dev/null || true
fi

# Ensure all auxiliary Python modules (Ext) are available in the bundle
# Merge from multiple known locations without special-casing per module.
mkdir -p ${conda_env}/Ext

# 1) Copy any Ext content produced by the main build
if [[ -d ../../../build/release/Ext ]]; then
    cp -a ../../../build/release/Ext/* ${conda_env}/Ext/ 2>/dev/null || true
fi

# 2) Copy any Ext content produced by pixi build helpers (e.g., PySide shims)
if [[ -d ../.pixi/build/Ext ]]; then
    cp -a ../.pixi/build/Ext/* ${conda_env}/Ext/ 2>/dev/null || true
fi

# 3) Fallback: copy pure-Python third-party modules from source tree into Ext if missing
if [[ -d ../../../src/3rdParty ]]; then
    for pkg in ../../../src/3rdParty/*; do
        base_name=$(basename "$pkg")
        # Skip non-directories and CMakeLists etc.
        [[ -d "$pkg" ]] || continue
        [[ -e "$pkg/CMakeLists.txt" ]] || true
        # Only copy if it looks like a Python package/module and not already present in Ext
        if [[ ! -e ${conda_env}/Ext/${base_name} ]]; then
            if ls "$pkg"/*.py >/dev/null 2>&1 || [[ -f "$pkg/__init__.py" ]]; then
                mkdir -p ${conda_env}/Ext/${base_name}
                cp -a "$pkg"/*.py ${conda_env}/Ext/${base_name}/ 2>/dev/null || true
                [[ -f "$pkg/__init__.py" ]] && cp -a "$pkg/__init__.py" ${conda_env}/Ext/${base_name}/ 2>/dev/null || true
            fi
        fi
    done
fi


export PATH="${PWD}/${conda_env}/bin:${PATH}"
export CONDA_PREFIX="${PWD}/${conda_env}"

# delete unnecessary stuff
rm -rf ${conda_env}/include
find ${conda_env} -name \*.a -delete

rm -rf ${conda_env}/bin_tmp
mv ${conda_env}/bin ${conda_env}/bin_tmp
mkdir ${conda_env}/bin
# freecad / FreeCAD
if [[ -f ${conda_env}/bin_tmp/freecad ]]; then
  cp ${conda_env}/bin_tmp/freecad ${conda_env}/bin/freecad
elif [[ -f ${conda_env}/bin_tmp/FreeCAD ]]; then
  cp ${conda_env}/bin_tmp/FreeCAD ${conda_env}/bin/freecad
fi

# freecadcmd / FreeCADCmd
if [[ -f ${conda_env}/bin_tmp/freecadcmd ]]; then
  cp ${conda_env}/bin_tmp/freecadcmd ${conda_env}/bin/freecadcmd
elif [[ -f ${conda_env}/bin_tmp/FreeCADCmd ]]; then
  cp ${conda_env}/bin_tmp/FreeCADCmd ${conda_env}/bin/freecadcmd
fi

# вспомогательные — только если существуют
for tool in ccx python pip pyside6-rcc gmsh dot unflatten; do
  [[ -f ${conda_env}/bin_tmp/${tool} ]] && cp ${conda_env}/bin_tmp/${tool} ${conda_env}/bin/
done

rm -rf ${conda_env}/bin_tmp

sed -i '' '1s|.*|#!/usr/bin/env python|' ${conda_env}/bin/pip

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
mkdir -p ARCHI.app/Contents/MacOS
cp build/ARCHI ARCHI.app/Contents/MacOS/ARCHI

# Ad-hoc sign development builds to stabilize Keychain/Code Requirement
SIGN_DEV=${SIGN_DEV:-true}
if [[ "${SIGN_RELEASE}" != "true" && "${SIGN_DEV}" == "true" ]]; then
  echo "Ad-hoc signing development bundle..."
  function run_codesign_adhoc {
    /usr/bin/codesign --options runtime -f -s - --timestamp=none --entitlements entitlements.plist "$1"
  }
  IFS=$'\n'
  dylibs=($(/usr/bin/find "ARCHI.app" -name "*.dylib"))
  shared_objects=($(/usr/bin/find "ARCHI.app" -name "*.so"))
  bundles=($(/usr/bin/find "ARCHI.app" -name "*.bundle"))
  executables=($(/usr/bin/find "ARCHI.app" -type f -perm +111 -exec file {} + | grep "Mach-O 64-bit executable" | sed 's/:.*//g'))
  IFS=$' \t\n'
  signed_files=("${dylibs[@]}" "${shared_objects[@]}" "${bundles[@]}" "${executables[@]}")
  for exe in ${signed_files}; do
    run_codesign_adhoc "${exe}" || true
  done
  run_codesign_adhoc "ARCHI.app/Contents/packages.txt" || true
  run_codesign_adhoc "ARCHI.app/Contents/Library/QuickLook/QuicklookFCStd.qlgenerator/Contents/MacOS/QuicklookFCStd" || true
  run_codesign_adhoc "ARCHI.app"
  /usr/bin/codesign --verify --deep --strict --verbose=2 "ARCHI.app" | cat || true
fi

python_version=$(python -c 'import platform; print("py" + platform.python_version_tuple()[0] + platform.python_version_tuple()[1])')
version_name="ARCHI_${BUILD_TAG}-macOS-$(uname -m)-${python_version}"
application_menu_name="ARCHI_${BUILD_TAG}"

echo -e "\################"
echo -e "version_name:  ${version_name}"
echo -e "################"

cp Info.plist.template ${conda_env}/../Info.plist
sed -i '' "s/FREECAD_VERSION/${version_name}/" ${conda_env}/../Info.plist
sed -i '' "s/APPLICATION_MENU_NAME/${application_menu_name}/" ${conda_env}/../Info.plist

pixi list -e package > ARCHI.app/Contents/packages.txt
sed -i '' '1s/.*/\nLIST OF PACKAGES:/' ARCHI.app/Contents/packages.txt

# copy the plugin into its final location
if [[ -d ${conda_env}/Library ]]; then
  cp -a ${conda_env}/Library ${conda_env}/..
  rm -rf ${conda_env}/Library
fi


# create the signed dmg with a progress bar
if [[ "${SIGN_RELEASE}" == "true" ]]; then
    echo -e "Creating signed DMG..."
    ./macos_sign_and_notarize.zsh -p "ARCHI" -k "${SIGNING_KEY_ID}" -o "${version_name}.dmg" | while IFS= read -r line; do
        echo -e "\r[In progress] $line"
    done
    echo -e "\nSigned DMG creation complete."
else
    # create the dmg using the rattler-build Pixi environment explicitly with a progress bar
    echo -e "Building DMG..."
    pixi run -e package -- python -m dmgbuild -s dmg_settings.py "ARCHI" "${version_name}.dmg" | while IFS= read -r line; do
        echo -e "\r[In progress] $line"
    done
    echo -e "\nDMG build complete."
fi


# create hash
sha256sum "../../../build/bundle/${version_name}.dmg" > "../../../build/bundle/${version_name}.dmg-SHA256.txt"

if [[ "${UPLOAD_RELEASE}" == "true" ]]; then
    gh release upload --clobber ${BUILD_TAG} "../../../build/bundle/${version_name}.dmg" "../../../build/bundle/${version_name}.dmg-SHA256.txt"
fi