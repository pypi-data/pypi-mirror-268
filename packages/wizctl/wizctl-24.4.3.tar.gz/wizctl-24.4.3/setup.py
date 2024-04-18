#
#   Copyright 2020 The SpaceONE Authors.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from setuptools import setup, find_packages

with open('VERSION', 'r') as f:
    VERSION = f.read().strip()
    f.close()

setup(
    name='wizctl',
    version=VERSION,
    description='CloudWiz Command Line Interface',
    long_description='',
    url='https://cloudwiz.ktds.com/',
    author='Cloudwiz Team',
    author_email='admin@cloudwiz.ktds.com',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        'kt-ds-core',
        'kt-ds-api',
        'Click',
        'tabulate',
        'jinja2',
        'gspread',
        'pandas',
        'google-api-core',
        'google-api-python-client',
        'oauth2client',
        'boto3',
        'PyMySQL'
    ],
    package_data={
        'spacectl': ['template/*.yml']
    },
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'wizctl = spacectl.main:main',
        ]
    },
)
