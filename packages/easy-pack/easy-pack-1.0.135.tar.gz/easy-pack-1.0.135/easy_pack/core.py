import os
import sys
import json
from .files.resources import Resources


class EasyPackModule:
    def __init__(self,
                 major=0,
                 minor=0,
                 build=0,
                 source_folder="source_folder",
                 module_name="module_name",
                 package_name="package_name",
                 author="author",
                 author_email="author@email",
                 description="",
                 install_requires="",
                 license_type="",
                 url="",
                 license_file="",
                 readme_file=""):

        if install_requires is None:
            install_requires = []

        self.module_info = {"major": major,
                            "minor": minor,
                            "build": build,
                            "source_folder": source_folder,
                            "module_name": module_name,
                            "package_name": package_name,
                            "author": author,
                            "author_email": author_email,
                            "description": description,
                            "install_requires": install_requires,
                            "license_type": license_type,
                            "url": url,
                            "license_file": license_file,
                            "readme_file": readme_file}

    def version_string(self):
        return "%i.%i.%i" % (self.module_info["major"], self.module_info["minor"], self.module_info["build"])

    def module_file(self):
        return "%s-%s" % (self.module_info["module_name"], self.version_string())

    def save(self, folder: str):
        with open(os.path.join(folder, "module_info.txt"), 'w') as f:
            json.dump(self.module_info, f, indent=4)
        return True

    @staticmethod
    def read(folder):
        #backward compatibility:
        old_module_file = os.path.join(folder, "__info__.py")
        module_file = os.path.join(folder, "module_info.txt")
        if os.path.exists(old_module_file):
            convert_old_module_file(old_module_file, module_file)

        if os.path.exists(module_file):
            with open(module_file, 'r') as f:
                module_info_data = json.load(f)
            module = EasyPackModule(**module_info_data)
            return module
        else:
            return None

    def get_setup(self):
        setup_py = "from setuptools import setup\n"
        setup_py += "\nsetup(name='" + self.module_info["package_name"] + "',\n"
        if self.module_info["description"]:
            setup_py += "      description='" + self.module_info["description"] + "',\n"
        if self.module_info["url"]:
            setup_py += "      url='" + self.module_info["url"] + "',\n"
        if self.module_info["author"]:
            setup_py += "      author='" + self.module_info["author"] + "',\n"
        if self.module_info["author_email"]:
            setup_py += "      author_email='" + self.module_info["author_email"] + "',\n"
        if self.module_info["readme_file"]:
            setup_py += "      long_description=open('./" + self.module_info["module_name"] + "/" + self.module_info["readme_file"].split("/")[-1] + "').read() + '\\n---\\n<small>Package created with Easy-pack</small>\\n',\n"
            setup_py += "      long_description_content_type='text/markdown',\n"
        if self.module_info["package_name"]:
            setup_py += "      packages=['" + self.module_info["module_name"] + "'],\n"
        if self.module_info["install_requires"]:
            setup_py += "      install_requires=" + str(self.module_info["install_requires"]) + ",\n"
        if self.module_info["license_type"]:
            setup_py += "      license='" + self.module_info["license_type"] + "',\n"
        setup_py += "      include_package_data=True,\n"
        setup_py += "      version='" + self.version_string() + "',\n"
        setup_py += "      zip_safe=False)\n"

        setup_cfg = "[metadata]\n"
        setup_cfg += "name = " + self.module_info["package_name"] + "\n"
        setup_cfg += "version = " + self.version_string() + "\n"
        if self.module_info["author"]:
            setup_cfg += "author = " + self.module_info["author"] + "\n"
        if self.module_info["description"]:
            setup_cfg += "description = " + self.module_info["description"] + "\n"
        if self.module_info["readme_file"]:
            setup_cfg += "description-file = " + self.module_info["readme_file"].split("/")[-1] + "\n"

        return setup_py, setup_cfg

    def create_setup_files(self, destination: str, module_folder: str):
        setup_py, setup_cfg = self.get_setup()
        with open(destination + "/setup.py" , "w") as m:
            m.writelines([setup_py])
        with open(module_folder + "/setup.cfg", "w") as m:
            m.writelines([setup_cfg])

    def build_module(self, dst):
        init_file_path = os.path.join(self.module_info["source_folder"], "__init__.py")
        if not os.path.exists(init_file_path):
            return False

        if not os.path.exists(dst):
            os.mkdir(dst)

        destination = dst + "/" + self.module_file()

        if not os.path.exists(destination):
            os.mkdir(destination)

        from shutil import copy, copytree

        module_folder = destination + "/" + self.module_info["module_name"]

        copytree(self.module_info["source_folder"], module_folder)

        if not os.path.exists(module_folder):
            os.mkdir(module_folder)

        open(destination + "/MANIFEST.in", "w").write("recursive-include " + self.module_info["module_name"] + " *\n")

        if self.module_info["readme_file"]:
            copy(os.path.join(self.module_info["source_folder"], self.module_info["readme_file"]), module_folder)
            copy(os.path.join(self.module_info["source_folder"], self.module_info["readme_file"]), destination)

        if self.module_info["license_file"]:
            copy(os.path.join(self.module_info["source_folder"], self.module_info["license_file"]), module_folder)

        self.create_setup_files(destination=destination, module_folder=module_folder)

        import subprocess
        import sys
        p = subprocess.Popen([sys.executable, "setup.py", "sdist"], cwd=destination)
        p.wait()
        self.module_info["build"] += 1
        return destination


def convert_old_module_file(old_module_file, new_module_file):
    folder = os.path.dirname(old_module_file)
    must_remove = False
    if folder not in sys.path:
        sys.path.append(folder)
        must_remove = True
    import __info__ as info
    content = vars(info)
    if "__module_version__" in content:
        major, minor, build = info.__module_version__()
    else:
        major, minor, build = 0, 0, 0
    if "__module_name__" in content:
        module_name = info.__module_name__()
    else:
        module_name = ""
    if "__package_name__" in content:
        package_name = info.__package_name__()
    else:
        package_name = ""
    if "__author__" in content:
        author = info.__author__()
    else:
        author = ""
    if "__description__" in content:
        description = info.__description__()
    else:
        description = ""
    if "__install_requires__" in content:
        install_requires = info.__install_requires__()
    else:
        install_requires = ""
    if "__license__" in content:
        license_type = info.__license__()
    else:
        license_type = ""
    if "__author_email__" in content:
        author_email = info.__author_email__()
    else:
        author_email = ""
    if "__license_file__" in content:
        license_file = info.__license_file__()
    else:
        license_file = ""
    if "__readme_file__" in content:
        readme_file = info.__readme_file__()
    else:
        readme_file = ""
    if "__url__" in content:
        url = info.__url__()
    else:
        url = ""

    if "__root_folder__" in content:
        source_folder = info.__root_folder__()
    else:
        source_folder = ""

    if must_remove:
        sys.path.remove(folder)

    module_info = {"major": major,
                   "minor": minor,
                   "build": build,
                   "source_folder": source_folder,
                   "module_name": module_name,
                   "package_name": package_name,
                   "author": author,
                   "author_email": author_email,
                   "description": description,
                   "install_requires": install_requires,
                   "license_type": license_type,
                   "url": url,
                   "license_file": license_file,
                   "readme_file": readme_file}

    with open(new_module_file, 'w') as f:
        json.dump(module_info, f, indent=4)

    os.rename(old_module_file, os.path.join(folder, "__info__.back"))
