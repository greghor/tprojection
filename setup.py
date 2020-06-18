#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ "pandas>=0.22", "numpy>=1.13.3", "seaborn>=0.9.0", "pytest>=5.3.2", "matplotlib>=3.1.2"]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Gregoire Hornung",
    author_email='greghor4@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Visualize the relation between a dependent variable and a predictor in a meaningful way",
    install_requires=requirements,
    license="MIT license",
#    long_description=readme + '\n\n' + history,
    long_description=readme,
    include_package_data=True,
    keywords='tprojection',
    name='tprojection',
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/greghor/tprojection',
    version='0.2.4',
    zip_safe=False,
)
