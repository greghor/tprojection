
tprojection
===========


.. image:: https://badge.fury.io/py/tprojection.svg
   :target: https://badge.fury.io/py/tprojection
   :alt: PyPI version


.. image:: https://travis-ci.com/greghor/tprojection.svg?branch=master
   :target: https://travis-ci.com/github/greghor/tprojection
   :alt: Build Status


.. image:: https://img.shields.io/codecov/c/github/greghor/tprojection
   :target: https://img.shields.io/codecov/c/github/greghor/tprojection
   :alt: Code cov


This library allows you to visually inspect the relation between a dependent variable (the
target) and a predictor in a meaningful way. This library is particularly convenient when the
target and/or the predictor are categorical, ie when it is difficult to compute a traditionnal correlation coefficient.
And by the way, Tprojection stands for target projection.

Installation
------------

.. code-block::

   pip install tprojection


Basic usage
-----------

.. code-block::

    from tprojection import Tprojection

    tproj = Tprojection(df, "target", "predictor")
    tproj.plot()


Advanced usage
--------------

You can find several examples depicting more advanced functionalities in ``examples/examples.ipynb``

Credits
-------

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ and the `cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`_ project template.
