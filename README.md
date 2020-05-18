# tprojection


<div class="row">

<img src="examples/survived_cabin.png" height="250" width="385">
<img src="examples/fare_cabin.png" height="250" width="385">
<img src="examples/survived_fare.png" height="250" width="385">
<img src="examples/fare_age.png" height="250" width="385">

<div class="row">
</div>


[![pypi] (https://img.shields.io/pypi/v/tprojection.svg)] (https://pypi.python.org/pypi/tprojection)
[![Build Status](https://travis-ci.org/mwaskom/seaborn.svg?branch=master)](https://travis-ci.org/mwaskom/seaborn)
![Code cov](https://img.shields.io/codecov/c/github/greghor/tprojection)


Tprojection stands for target projection. This library allows you to visually inspect the relation between a dependent variable (the target) and a predictor in a meaningful way. This library is particularly convenient when it is difficult to compute a traditionnal correlation coefficient, for instance when either the target or the predictor is categorical.
And by the way, Tprojection stands for target projection.


## Installation

    pip install tprojection

## Basic usage

     from tprojection import Tprojection

     tproj = Tprojection(df, "target", "predictor")
     tproj.plot()

## Advanced usage

You can find several examples of more advanced tprojection functionalities in `examples/examples.ipynb`

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.

