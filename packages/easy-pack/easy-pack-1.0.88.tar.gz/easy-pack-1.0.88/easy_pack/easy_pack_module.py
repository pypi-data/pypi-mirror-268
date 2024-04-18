import os
import sys


def get_module_folder() -> str:
    import importlib.util

    spec = importlib.util.find_spec('easy_pack')
    if spec:
        return spec.submodule_search_locations[0].replace("\\","/").replace("//","/")
    else:
        return "."

class EasyPackModule:

    def __init__(self,
                 build_number=0,
                 module_name="module_name",
                 package_name="package_name",
                 author="author",
                 author_email="author@email",
                 description="",
                 install_requires="",
                 license="",
                 url="",
                 license_file="",
                 readme_file="",
                 setup_py="",
                 setup_cfg="",
                 folder=""):
        self.major = 0
        self.minor = 0
        self.build_number = build_number
        self.module_name = module_name
        self.package_name = package_name
        self.author = author
        self.author_email = author_email
        self.description = description
        if install_requires is None:
            self.install_requires = []
        else:
            self.install_requires = install_requires
        self.license = license
        self.url = url
        self.license_file = license_file
        self.readme_file = readme_file
        self.setup_py = setup_py
        self.setup_cfg = setup_cfg
        self.root_folder = folder

    def version_string(self):
        return str(self.major) + "." + str(self.minor) + "." + str(self.build_number)

    def package_file(self):
        return self.package_name + "-" + self.version_string()

    def get_module_info_file(self):
        module_info_script = ""
        module_info_script += "def __module_version__():\n"
        module_info_script += "\treturn " + str(self.major) + ", " + str(self.minor) + ", " + str(self.build_number) + " \n\n\n"
        module_info_script += "def __module_name__():\n"
        module_info_script += "\treturn '" + self.module_name + "' \n\n\n"
        module_info_script += "def __author__():\n"
        module_info_script += "\treturn '" + self.author + "' \n\n\n"
        module_info_script += "def __author_email__():\n"
        module_info_script += "\treturn '" + self.author_email + "' \n\n\n"
        module_info_script += "def __package_description__():\n"
        module_info_script += "\treturn '" + self.description + "' \n\n\n"
        module_info_script += "def __install_requires__():\n"
        module_info_script += "\treturn " + str(self.install_requires) + " \n\n\n"
        module_info_script += "def __url__():\n"
        module_info_script += "\treturn '" + self.url + "' \n\n\n"
        module_info_script += "def __license__():\n"
        module_info_script += "\treturn '" + self.license + "' \n\n\n"
        module_info_script += "def __license_file__():\n"
        module_info_script += "\treturn '" + self.license_file + "' \n\n\n"
        module_info_script += "def __readme_file__():\n"
        module_info_script += "\treturn '" + self.readme_file + "' \n\n\n"
        module_info_script += "def __package_name__():\n"
        module_info_script += "\treturn '" + self.package_name + "' \n\n\n"
        module_info_script += "def __setup_py__():\n"
        module_info_script += "\treturn '" + self.setup_py + "' \n\n\n"
        module_info_script += "def __setup_cfg__():\n"
        module_info_script += "\treturn '" + self.setup_cfg + "' \n\n\n"
        module_info_script += "def __root_folder__():\n"
        module_info_script += "\treturn '" + self.root_folder + "' \n\n\n"
        module_info_script += "def __description__():\n"
        module_info_script += "\treturn '" + self.description + "' \n\n\n"
        return module_info_script

    def save(self, folder):
        with open(folder + "/__info__.py", "w") as v:
            v.write(self.get_module_info_file())
        return True

    @staticmethod
    def scaffold(folder='.',
                 module_name='src'):
        if not os.path.exists(folder):
            os.mkdir(folder)
        src = folder + "/" + module_name
        resources = folder + "/resources"
        license = resources + "/license.txt"
        readme = resources + "/README.md"
        files = src + "/files"
        init = src + "/__init__.py"
        build = folder + "/build.py"
        if not os.path.exists(src):
            os.mkdir(src)
        if not os.path.exists(init):
            with open(init, "w") as f:
                f.writelines(["#add imports here"])
        if not os.path.exists(resources):
            os.mkdir(resources)
        if not os.path.exists(license):
            with open(license, "w") as f:
                f.writelines(["write your license agreement here"])
        if not os.path.exists(readme):
            with open(readme, "w") as f:
                f.writelines(["#Add your readme in markdown format here"])
        module = EasyPackModule(readme_file='../resources/README.md',
                                license_file='../resources/license.txt',
                                folder=module_name)
        if not os.path.exists(files):
            os.mkdir(files)
        module.save(folder)
        from shutil import copy
        module_folder = get_module_folder()
        build_file = module_folder + "/files/build.py"
        copy (build_file, build)

    @staticmethod
    def read(folder):
        if os.path.exists(folder + "/__info__.py"):
            must_remove = False
            if folder not in sys.path:
                sys.path.append(folder)
                must_remove = True
            import __info__ as info
            content = vars(info)
            module_info = EasyPackModule()
            if "__module_version__" in content:
                module_info.major, module_info.minor, module_info.build_number = info.__module_version__()
            if "__module_name__" in content:
                module_info.module_name = info.__module_name__()
            if "__package_name__" in content:
                module_info.package_name = info.__package_name__()
            if "__author__" in content:
                module_info.author = info.__author__()
            if "__description__" in content:
                module_info.description = info.__description__()
            if "__install_requires__" in content:
                module_info.install_requires = info.__install_requires__()
            if "__license__" in content:
                module_info.license = info.__license__()
            if "__author_email__" in content:
                module_info.author_email = info.__author_email__()
            if "__license_file__" in content:
                module_info.license_file = info.__license_file__()
            if "__readme_file__" in content:
                module_info.readme_file = info.__readme_file__()
            if "__setup_py__" in content:
                module_info.setup_py = info.__setup_py__()
            if "__setup_cfg__" in content:
                module_info.setup_cfg = info.__setup_cfg__()
            if "__root_folder__" in content:
                module_info.root_folder = info.__root_folder__()
            if "__url__" in content:
                module_info.url = info.__url__()
            if must_remove:
                sys.path.remove(folder)
            return module_info
        else:
            return None

    def get_setup(self):
        setup_py = "from setuptools import setup\n"
        setup_py += "\nsetup(name='" + self.module_name + "',\n"
        if self.description:
            setup_py += "      description='" + self.description + "',\n"
        if self.url:
            setup_py += "      url='" + self.url + "',\n"
        if self.author:
            setup_py += "      author='" + self.author + "',\n"
        if self.author_email:
            setup_py += "      author_email='" + self.author_email + "',\n"
        if self.readme_file:
            setup_py += "      long_description=open('./" + self.package_name + "/" + self.readme_file.split("/")[-1] + "').read(),\n"
            setup_py += "      long_description_content_type='text/markdown',\n"
        if self.package_name:
            setup_py += "      packages=['" + self.package_name + "'],\n"
        if self.install_requires:
            setup_py += "      install_requires=" + str(self.install_requires) + ",\n"
        if self.license:
            setup_py += "      license='" + self.license + "',\n"
        setup_py += "      include_package_data=True,\n"
        setup_py += "      version='" + self.version_string() + "',\n"
        setup_py += "      zip_safe=False)\n"

        setup_cfg = "[metadata]\n"
        setup_cfg += "name = " + self.module_name + "\n"
        setup_cfg += "version = " + self.version_string() + "\n"
        if self.author:
            setup_cfg += "author = " + self.author + "\n"
        if self.description:
            setup_cfg += "description = " + self.description + "\n"
        if self.readme_file:
            setup_cfg += "description-file = " + self.readme_file.split("/")[-1] + "\n"

        return setup_py, setup_cfg

    def create_setup_files(self, destination: str, module_folder: str):
        setup_py, setup_cfg = self.get_setup()
        with open(destination + "/setup.py" , "w") as m:
            m.writelines([setup_py])
        with open(module_folder + "/setup.cfg", "w") as m:
            m.writelines([setup_cfg])

    def build_module(self, dst):

        if not os.path.exists(self.root_folder + "/__init__.py"):
            return False

        if not self.setup_py:
            return False

        if not self.setup_cfg:
            return False

        if not os.path.exists(dst):
            os.mkdir(dst)


        destination = dst + "/" + self.package_file()

        if not os.path.exists(destination):
            os.mkdir(destination)

        from shutil import copy, copytree

        module_folder = destination + "/" + self.package_name

        copytree(self.root_folder, module_folder)

        if not os.path.exists(module_folder):
            os.mkdir(module_folder)

        open(destination + "/MANIFEST.in", "w").write("recursive-include " + self.package_name + " *\n")

        if self.readme_file:
            copy(self.root_folder + "/" + self.readme_file, module_folder)
            copy(self.root_folder + "/" + self.readme_file, destination)

        if self.license_file:
            copy(self.root_folder + "/" + self.license_file, module_folder)

        self.create_setup_files(destination=destination, module_folder=module_folder)

        import subprocess
        import sys
        p = subprocess.Popen([sys.executable, "setup.py", "sdist"], cwd=destination)
        p.wait()
        self.build_number += 1
        return destination
