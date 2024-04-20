from setuptools import setup, find_packages

setup(
    name='medicafe',
    version='0.240419.1',
    description='MediCafe',
    long_description='This module ensures that MediCafe remains up-to-date by performing version checks for its dependencies on startup. It utilizes PyPI, the official repository for Python packages, to retrieve information about the latest available versions of the required packages. When an internet connection is available, MediUpdate automatically installs any available updates using pip, the package installer for Python.',
    long_description_content_type='text/markdown',
    keywords = 'medicafe python34 medibot medilink',
    url='https://github.com/katanada2',
    author='Daniel Vidaud',
    author_email='daniel@personalizedtransformation.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'MediCafe.MediBot': ['*.bat'],
        'MediCafe.MediLink_batch': ['*.bat']
    },
    install_requires=[
        'requests',
        'argparse',
        'numpy==1.11.3',
        'pandas==0.20.0',
        'tqdm==4.14.0'
    ],
    zip_safe=False
)