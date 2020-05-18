tprojection
===========
<div class="row">

<a href=https://seaborn.pydata.org/examples/scatterplot_matrix.html>
<img src="https://seaborn.pydata.org/_static/scatterplot_matrix_thumb.png" height="135" width="135">
</a>

<a href=https://seaborn.pydata.org/examples/errorband_lineplots.html>
<img src="https://seaborn.pydata.org/_static/errorband_lineplots_thumb.png" height="135" width="135">
</a>

<a href=https://seaborn.pydata.org/examples/different_scatter_variables.html>
<img src="https://seaborn.pydata.org/_static/different_scatter_variables_thumb.png" height="135" width="135">
</a>

<a href=https://seaborn.pydata.org/examples/many_facets.html>
<img src="https://seaborn.pydata.org/_static/many_facets_thumb.png" height="135" width="135">
</a>

<a href=https://seaborn.pydata.org/examples/structured_heatmap.html>
<img src="https://seaborn.pydata.org/_static/structured_heatmap_thumb.png" height="135" width="135">
</a>

<a href=https://seaborn.pydata.org/examples/horizontal_boxplot.html>
<img src="https://seaborn.pydata.org/_static/horizontal_boxplot_thumb.png" height="135" width="135">
</a>

</div>

.. image:: https://img.shields.io/pypi/v/tprojection.svg
        :target: https://pypi.python.org/pypi/tprojection

.. image:: https://img.shields.io/travis/greghor/tprojection.svg
        :target: https://travis-ci.org/greghor/tprojection

[![Build Status](https://travis-ci.org/mwaskom/seaborn.svg?branch=master)](https://travis-ci.org/mwaskom/seaborn)

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
