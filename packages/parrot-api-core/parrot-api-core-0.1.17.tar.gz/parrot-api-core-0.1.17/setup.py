#!/usr/bin/env python

"""The setup script."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

with open('requirements_dev.txt') as test_requirements_file:
    test_requirements = test_requirements_file.read()



setup(
    author="Perry Stallings",
    author_email='astal01@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python API Project Framework",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='parrot_api_core',
    name='parrot-api-core',
    packages=['parrot_api.core', 'parrot_api.core.auth', 'parrot_api.core.auth.providers'],
    test_suite='tests',
    extras_require={},
    tests_require=test_requirements,
    url='https://github.com/perrystallings/parrot_api_core',
    version='0.1.17',
    zip_safe=False
)
