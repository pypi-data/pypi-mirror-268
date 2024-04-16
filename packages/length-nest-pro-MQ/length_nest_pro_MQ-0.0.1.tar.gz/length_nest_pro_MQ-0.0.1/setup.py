from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'length_nest_pro_MQ'
LONG_DESCRIPTION = 'An adapted version of the length nest pro, enriched with a message queue connection'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="length_nest_pro_MQ",
    version=VERSION,
    author="Niels Bos",
    author_email="nielsb00@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "numpy",
        "wheel",
        "setuptools",
        "pika"
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)