#!/usr/bin/env python

"""Tests for `tprojection` package."""

##{
import pytest
from numpy.random import *
import pandas as pd
from tprojection.core import Tprojection
from tprojection.datasets import load_data
##}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

##{
df = load_data("titanic")
target = "survived"
tproj = Tprojection(df, target, "sex", target_type="categorical", feature_type="categorical")
##}

def test_infer_survived_pclass_as_categorical():
    tproj = Tprojection(df, target, "pclass")
    assert tproj.target_type == 'categorical', 'target type shall be categorical'
    assert tproj.feature_type == 'categorical', 'feature type shall be categorical'

##{
def test_infer_age_fare_as_continuous():
    tproj = Tprojection(df, "age", "fare")
    assert tproj.target_type == 'continuous', 'target type shall be continuous'
    assert tproj.feature_type == 'continuous', 'feature type shall be continuous'
    ##}



##{
def test_categorical_feature_type_turned_to_obj():
    df = pd.DataFrame()
    df['target'] = randint(0, 2, 1000) 
    df['feature'] = randint(0, 5, 1000)

    tproj  = Tprojection(df, 'target', 'feature')
    assert isinstance(tproj.df.target.dtype, object), "feature type shall have turned to object"
    tproj._cat2all_prep()
    assert isinstance(tproj.dg.index.dtype, object), "plotted data index type shall bject"
##}


##{
df = load_data("titanic")
target = "survived"
tproj = Tprojection(df, target, "name", nb_modalities=10)
##}
