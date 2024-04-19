from setuptools import setup, find_packages  # type: ignore
import os
from package_readme import long_description
import re

# 0.1.0 is the 'version' installs from this directory from other components in repo will use
version = os.getenv('PACKAGE_VERSION')

if version is None:
    raise ValueError("PACKAGE_VERSION environment variable is not set")

if re.match(r'refs/tags/.*', version):
    version = version.replace('refs/tags/', '')
else:
    raise ValueError("PACKAGE_VERSION environment variable is not set correctly. Expecting 'refs/tags/*'. Got " + version + " instead")

setup(
    name='provena-interfaces',
    # format acceptably as 'v0.0.1' or '0.0.1',
    version=version,
    description='Interfaces for Provena Application (see https://provena.io)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(
        include=[
            'ProvenaInterfaces',
            'ProvenaInterfaces.*',
            'ProvenaInterfaces.*.*',
        ]
    ),
    install_requires=[
        'fastapi==0.88.0',
        'pydantic[email]==1.10.12',
        'email-validator',
        'isodate',
    ],
    package_data={
        'ProvenaInterfaces': ['py.typed']
    },
    url="https://provena.io",
    maintainer_email="rrap-mds-is-support@csiro.au",

)
