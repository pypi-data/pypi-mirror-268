from setuptools import setup

setup(
   name='tymer',
   version='1.0.4',
   description='A simple timer',
   author='Morris El Helou',
   author_email='morrishelou@gmail.com',
   include_package_data=True,
   packages=['tymer'], 
   package_data={"tymer": ["*.ico"]},
   install_requires=[], #external packages as dependencies
)