===========
tprojection
===========


.. image:: https://img.shields.io/pypi/v/tprojection.svg
        :target: https://pypi.python.org/pypi/tprojection

.. image:: https://img.shields.io/travis/greghor/tprojection.svg
        :target: https://travis-ci.org/greghor/tprojection

.. image:: https://readthedocs.org/projects/tprojection/badge/?version=latest
        :target: https://tprojection.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/codecov/c/github/greghor/tprojection   
        :alt: Codecov

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
