#!/usr/bin/env python

# Easy-Pack build tool
# Provides options to build, install, and upload a distribution package
# -install: Installs the package after build
# -upload: Uses twine to upload the package to PyPI
# -user: PyPI account username (required for upload)
# -password: PyPI security token (required for upload)
# -repository: PyPI repository URL (optional for upload)

import argparse
import sys
from .core import EasyPackModule
import subprocess


def parse_arguments():
    parser = argparse.ArgumentParser(description='Easy-Pack Builder: builds the module and creates a distribution package')
    parser.add_argument('-install', action='store_true', help='Install the package after build')
    parser.add_argument('-upload', action='store_true', help='Uses twine to upload the package to pypi')
    parser.add_argument('-user', type=str, help='pipy account username')
    parser.add_argument('-password', type=str, help='pipy security token')
    parser.add_argument('-repository', type=str, help='pypi-repository-url (optional)')
    args = parser.parse_args()
    if args.upload and (not args.user or not args.password):
        parser.error("upload requires --user and --password")
    return args


def install(build_folder: str):
    installation_args = [sys.executable, "-m", "pip", "install", "."]
    installation_process = subprocess.Popen(installation_args, cwd=build_folder)
    installation_process.wait()

def upload(build_folder: str,
           user: str,
           password: str,
           repository: str):
    upload_args = [sys.executable, "-m", "twine", "upload", "dist/*", "-u", user, "-p", password]
    if repository:
        upload_args.append('--repository-url')
        upload_args.append(repository)
    upload_process = subprocess.Popen(upload_args, cwd=build_folder)
    upload_process.wait()


def main():
    try:
        args = parse_arguments()

        module = EasyPackModule.read('.')
        build_folder = module.build_module('python-build')

        if not build_folder:
            print('build failed')
            return

        print('build succeded')
        module.save('.')
        if args.install:
            install(build_folder=build_folder)

        if args.upload:
            upload(build_folder=build_folder,
                   user=args.user,
                   password=args.password,
                   repository=args.repository)
        else:
            print('use python -m twine upload --repository-url [pypi-repository-url] dist/* to upload the package')

    except argparse.ArgumentError as e:
        print("Error:", e)
        exit(1)

if __name__ == "__main__":
    main()