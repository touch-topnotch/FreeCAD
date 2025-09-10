#!/usr/bin/env python3

import os
import sys
import subprocess
import re

def run_command(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

def fix_lib_paths(lib_dir):
    # Find all dylib files
    for root, dirs, files in os.walk(lib_dir):
        for file in files:
            if file.endswith('.dylib') and 'vecLibFort' not in file:
                lib_path = os.path.join(root, file)
                print(f"Processing {lib_path}")
                
                # Get current install name
                install_name = run_command(f'otool -D "{lib_path}"').strip().split('\n')[-1]
                if install_name == '':
                    continue
                
                # Get all dependencies
                deps = run_command(f'otool -L "{lib_path}"').strip().split('\n')[1:]
                
                # Fix each dependency
                for dep in deps:
                    dep = dep.strip().split()[0]
                    if dep.startswith('@rpath/'):
                        # Get the actual library name
                        lib_name = os.path.basename(dep)
                        # Create new install name with @loader_path
                        new_name = f'@loader_path/{lib_name}'
                        # Change the install name
                        run_command(f'install_name_tool -change "{dep}" "{new_name}" "{lib_path}"')
                
                # Fix the install name itself if it's an @rpath
                if install_name.startswith('@rpath/'):
                    lib_name = os.path.basename(install_name)
                    new_name = f'@loader_path/{lib_name}'
                    run_command(f'install_name_tool -id "{new_name}" "{lib_path}"')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fix_macos_lib_paths.py <lib_directory>")
        sys.exit(1)
    
    lib_dir = sys.argv[1]
    if not os.path.exists(lib_dir):
        print(f"Error: Directory {lib_dir} does not exist")
        sys.exit(1)
    
    fix_lib_paths(lib_dir)