from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'ALAS utils for daily tasks'
LONG_DESCRIPTION = 'Eso'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ALASutils",
        version=VERSION,
        author="Juan Pablo Calderon",
        author_email="<jpcalderon@fcaglp.unlp.edu.ar>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'alas'],
        classifiers= [
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ])
