#Easy module_setup
A very opinionated single module packaging tool.

## Build, distribute and deploy modules easily.

###Create a new easy pack project
```
from easy_pack import EasyPackModule
EasyPackModule.scaffold(project_folder)
```
#### Produces the following output:
```
project_folder 
│   __info__.py        # module info file
│   build.py           # build script
│   
└───src                # module folder
│   │   __init__.py    # module 
│
└───resources
    │   license.txt    # license file (txt format)
    │   readme.md      # readme (mark-down format)
   
```

##The __info__.py file
All module properties are stored in the __info__.py file.
To customize your module, edit this file to match your code.

####Module version:
Returns a triplet with major, minor and build number
```
def __module_version__():
	return 0, 0, 1 
```

####Module name:
Returns a string with the name of the module 
```
def __module_name__():
	return 'module_name' 
```

####Author:
Returns a string with the name of the author (your name)
```
def __author__():
	return 'author' 
```

####Author email:
Returns a string with the email of the author (your email)
```
def __author_email__():
	return 'author@email'  
```

####Package description:
Returns a string with a brief description of your package
```
def __package_description__():
	return 'a brief description of your package'  
```


####Required packages:
Returns a list of strings with the packages your package is dependent on: 
```
def __install_requires__():
    return ['matplotlib', 'numpy']  
```

####Package url:
Returns a string with the url of your project (usually a github repository):
```
def __url__():
	return 'https://github.com/germanespinosa/easy-pack' 
```

####License type:
Returns a string with the license type (ie "MIT"):
```
def __license__():
	return 'MIT' 
```

####License file:
Returns a string with the relative path (from the module folder) to the license file: 
```
def __license_file__():
    return '../resources/license.txt' 
```


####Readme file:
Returns a string with the relative path (from the module folder) to the readme file:
```
def __readme_file__():
	return '../resources/README.md' 
```

####Package name:
Returns a string with the name of your package:
```
def __package_name__():
	return 'package_name' 
```

####Module description:
Returns a string with a brief description of your module:
```
def __description__():
    return 'a brief description of your module' 
```

###Building the package:
After modifying the __info__.py file to mach your module run:
```
python build.py 
```

#### Produces the following output:
```
project_folder 
│   
└───python-build                              
    └───package_name-version                  # build folder
        └───dist
        │   │   package_name-version.tar.gz   # package
        └───package_name                      # unpacked files
        │   │   package_file_01               
        │   │   package_file_02  
        │   │   package_file_03  
        │   │   package_file_04  
        └───package_name.egg-info             # supporting files
        │   │   dependency_links.txt  
        │   │   not-zip-safe
        │   │   PKG-INFO  
        │   │   requires.txt  
        │   │   SOURCES.txt  
        │   │   top_level.txt  
        │   README.md                         # readme file
        │   setup.py                          # setup
        
```

### Uploading your package to pypi
To upload your package to pypi you will need a (https://pypi.org/) account.
from the build folder run:
```
 twine upload dist/*
```
you will be asked username and password.


### Testing your package
From any computer with pip installed run:
```
pip install [package_name]
```
Once the installation is finished, open python and try importing your module:
```
import [module_name] 
```

# You are all done