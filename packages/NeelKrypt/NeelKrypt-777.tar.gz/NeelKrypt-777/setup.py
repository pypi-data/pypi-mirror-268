from setuptools import setup, find_packages

VERSION = '777' 
DESCRIPTION = 'Text Enkryptor and Dekryptor using PKI'
LONG_DESCRIPTION = 'USES DIFFIE HELLMAN @ CORE . KEY HANDLING AND CONVERSION IS THE ART HERE'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="NeelKrypt", 
        version=VERSION,
        author="Neelanjan Manna",
        author_email="nm3897mel@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pycryptodome'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'Diifie Pager', 'Auguste Kerckhoffs'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)