from tprojection.datasets import load_data
from tprojection.utils import *

df = load_data("titanic")
thresh = 0.05

def test_age_is_continuous():
    feat = "age"
    expected = True
    actual = is_continuous(df[feat], thresh)
    assert actual == expected, "age shall be considered as continuous"

def test_fare_is_continuous():
    feat = "fare"
    expected = True
    actual = is_continuous(df[feat], thresh)
    assert actual == expected, "fare shall be considered as continuous"

def test_name_is_not_continuous():
    feat = "name"
    expected = False
    actual = is_continuous(df[feat], thresh)
    assert actual == expected, "name shall be considered as categorical"

def test_pclass_is_not_continuous():
    feat = "pclass"
    expected = False
    actual = is_continuous(df[feat], thresh)
    assert actual == expected, "pclass shall be considered as categorical"


