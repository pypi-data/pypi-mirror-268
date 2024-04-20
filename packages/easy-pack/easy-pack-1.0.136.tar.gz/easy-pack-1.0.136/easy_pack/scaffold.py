#!/usr/bin/env python

# Easy-Pack scaffold tool
# Creates a new Easy-Pack project structure in the current folder
# - package_name: Name of the package as it will be called from pip
# - module_name: Name of the module as it will be imported in Python (default: package_name)
# - source_folder: Folder containing the module files, if already exists (default: module_name)
# - resources_file: Include the resource file locator helper (default: NO)
# - mit_license: Use the MIT license agreement (default: YES)
#
# This script automates the creation of an Easy-Pack project structure,
# enabling developers to quickly scaffold a new Python project with customizable options.
# It generates the necessary folder structure, copies essential files such as README.md and license.txt,
# and sets up the module and package configurations based on the provided arguments.

import argparse
import os
from .core import EasyPackModule
from .files.resources import Resources

def parse_arguments():
    parser = argparse.ArgumentParser(description='Easy-Pack Scaffold: creates a new easy_pack project structure on the current folder')
    parser.add_argument('package_name', type=str, help='name of the package as it will called from pip')
    parser.add_argument('-module_name', type=str, help='name of the module as it will be imported in python (default: package_name)', required=False)
    parser.add_argument('-source_folder', type=str, help='folder containing the module files, if already exists (default: module_name)', required=False)
    parser.add_argument('-resources_file', action='store_true', help='include the resource file locator helper (default: NO)')
    parser.add_argument('-mit_license', action='store_true', help='use the MIT license agreement (default: YES)')
    args = parser.parse_args()
    return args


def main():
    try:
        args = parse_arguments()

        folder = "."

        if args.module_name:
            module_name = args.module_name
        else:
            module_name = args.package_name

        if args.source_folder:
            source_folder = args.source_folder
        else:
            source_folder = module_name

        src_folder = os.path.join(folder, source_folder)

        if not os.path.exists(src_folder):
            os.mkdir(src_folder)

        additional_files_folder = os.path.join(src_folder, "files")

        if not os.path.exists(additional_files_folder):
            os.mkdir(additional_files_folder)

        from shutil import copy
        resources_folder = os.path.join(folder, "resources")
        if not os.path.exists(resources_folder):
            os.mkdir(resources_folder)

        readme_file_path = os.path.join(resources_folder, "README.md")
        if not os.path.exists(readme_file_path):
            copy(Resources.file("README.md"), resources_folder)

        license_file_path = os.path.join(resources_folder, "license.txt")
        license_type = ""
        if not os.path.exists(license_file_path):
            if args.mit_license:
                copy(Resources.file("license_MIT.txt"), license_file_path)
                license_type = "MIT"
            else:
                copy(Resources.file("license.txt"), resources_folder)

        copy(Resources.file("init.py"), os.path.join(src_folder, "__init__.py"))
        if args.resources_file:
            copy(Resources.file("resources.py"), src_folder)

        module = EasyPackModule(readme_file='../resources/README.md',
                                license_file='../resources/license.txt',
                                source_folder=source_folder,
                                module_name=module_name,
                                package_name=args.package_name,
                                license_type=license_type)
        module.save(folder)
    except argparse.ArgumentError as e:
        print("Error:", e)
        exit(1)


if __name__ == "__main__":
    main()
