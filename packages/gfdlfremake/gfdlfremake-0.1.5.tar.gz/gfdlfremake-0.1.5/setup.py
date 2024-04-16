from setuptools import setup, find_namespace_packages

setup(
    name='gfdlfremake',
    version='0.1.5',
    description='Implementation of fremake',
    author='Thomas Robinson, Dana Singh',
    author_email='gfdl.climate.mode.info@noaa.gov',
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=[
        'pyyaml',
        'argparse',
        'jsonschema',
    ],
)
