from setuptools import setup, find_packages

VERSION = '0.1.10' 
DESCRIPTION = 'CNS Scraping Package'
LONG_DESCRIPTION = 'CNS Scraping Package'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ResoluteCNS", 
        version=VERSION,
        author="Ryan Detlaff",
        author_email="rdetlaff@resolutecommercial.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        package_data={"":["./ResoluteCNS/uBlock0.xpi"]},
        include_package_data=True,
        install_requires=['selenium', 'pandas'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)