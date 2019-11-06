from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bmtools",
    version="0.0.1",
    author="Tyler Banks",
    author_email="tbanks@mail.missouri.edu",
    description="BMTools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tjbanks/bmtools",
    download_url='',
    license='MIT',
    install_requires=[
        'bmtk',
        'click',
        'clint',
        'h5py',
        'matplotlib',
        'networkx',
        'numpy',
        'pandas'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'bmtools = bmtools.cli.manage:cli'
        ]
    }
)