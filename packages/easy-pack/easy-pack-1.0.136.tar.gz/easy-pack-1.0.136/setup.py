from setuptools import setup

setup(name='easy-pack',
      description='easy packing!',
      url='https://github.com/germanespinosa/easy-pack',
      author='german espinosa',
      author_email='germanespinosa@gmail.com',
      long_description=open('./easy_pack/README.md').read() + '\n---\n<small>Package created with Easy-pack</small>\n',
      long_description_content_type='text/markdown',
      packages=['easy_pack'],
      install_requires=['twine'],
      license='MIT',
      include_package_data=True,
      version='1.0.136',
      zip_safe=False)
