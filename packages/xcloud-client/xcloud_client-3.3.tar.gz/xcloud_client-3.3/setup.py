from setuptools import setup, find_packages

setup(
    name='xcloud_client',
    version='3.3',
    packages=find_packages(),
    install_requires=[
        'JayDeBeApi==1.2.3'
    ],
    package_data={
        'xCloud_client': ['resources/*.jar']
    },
    include_package_data= True
    
)
