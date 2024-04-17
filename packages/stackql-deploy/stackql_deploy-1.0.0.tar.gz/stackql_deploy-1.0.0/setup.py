# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='stackql-deploy',
    version='1.0.0',
    description='Model driven resource provisioning and deployment framework using StackQL.',
    long_description=readme,
    author='Jeffrey Aven',
    author_email='javen@stackql.io',
    url='https://github.com/stackql/stackql-deploy',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 
        'python-dotenv',
        'jinja2',
        'pystackql'
        ],
    entry_points={
        'console_scripts': [
            'stackql-deploy = stackql_deploy.cli:cli',
        ],
    },
    classifiers=[
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
    ]
)