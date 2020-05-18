tprojection
===========

[![pypi] (https://img.shields.io/pypi/v/tprojection.svg)] (https://pypi.python.org/pypi/tprojection)
[![Build Status](https://travis-ci.org/mwaskom/seaborn.svg?branch=master)](https://travis-ci.org/mwaskom/seaborn)
[![Code cov](https://img.shields.io/codecov/c/github/greghor/tprojection)]

* Free software: MIT license

This library allows you to investigate the relation between a dependent variable and a predictor, irrepectively of their types (continuous vs categorical). This library is particularly useful
when both the dependent variable and the predictor are categorical. 


Installation
--------

    pip install tprojection

Basic usage
-------

     from tprojection import Tprojection

     tproj = Tprojection(df, "target", "predictor")
     tproj.plot()

Advanced usage
--------

You can find several examples of more advanced tprojection functionalities in examples/examples.ipynb

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
