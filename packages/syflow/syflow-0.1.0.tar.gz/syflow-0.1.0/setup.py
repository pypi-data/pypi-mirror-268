from skbuild_conan import setup
from setuptools import find_packages

setup(  # https://scikit-build.readthedocs.io/en/latest/usage.html#setup-options
    name="syflow",
    version="0.1.0",
    description="Real-Time PIV",
    author="Sam Foxman",
    author_email="sfoxman@caltech.edu",
    packages=find_packages("src"),  # Include all packages in `./src`.
    package_dir={"": "src"},  # The root for our python package is in `./src`.
    python_requires=">=3.7",  # lowest python version supported.
    install_requires=[],  # Python Dependencies
    cmake_minimum_required_version="3.23",
    cmake_args=["-DSYFLOW_PYTHON=ON"]
)