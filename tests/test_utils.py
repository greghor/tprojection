from tprojection.datasets import load_data
from tprojection.utils import *
import numpy as np
import numpy.random as rd   
import pandas as pd

df = load_data("titanic")
thresh = 0.05

##{
def test_age_is_continuous():
    feat = "age"
    expected = True
    actual = is_continuous(df[feat], thresh)
    assert actual == expected, "age shall be considered as continuous"
    ##}

##{
def test_fare_is_continuous():
    feat = "fare"
    expected = True
    actual = is_continuous(df[feat], thresh)
    assert actual == expected, "fare shall be considered as continuous"
    ##}

##{
def test_name_is_not_continuous():
    feat = "name"
    expected = False
    actual = is_continuous(df[feat], thresh)
    assert actual == expected, "name shall be considered as categorical"
    ##}

##{
def test_pclass_is_not_continuous():
    feat = "pclass"
    expected = False
    actual = is_continuous(df[feat], thresh)
    assert actual == expected, "pclass shall be considered as categorical"
    ##}


##{
def test_unbalanced_mod_freq_encoding():
    df = pd.DataFrame()
    mod = ['m' + str(int(x)) for x in np.linspace(0, 99, 100)] 
    p = [20, 20, 20] + [1]*97
    p = p/np.sum(p)
    n_obs = 1000
    df['feature'] = rd.choice(mod, size=n_obs, p=p)
    df['target'] = rd.choice([0, 1], size=n_obs, p=[0.9, 0.1])
    mymap = get_encoding(df, 'target', 'feature', nb_modalities=5)
    def myassert(x):
        assert mymap[x] == x, '{} shall be mapped to {}'.format(x, x)
    myassert('m0')
    myassert('m1')
    myassert('m2')
    ##}

##{
def test_balanced_mod_freq_encoding():
    df = pd.DataFrame()
    mod = ['m' + str(int(x)) for x in np.linspace(0, 99, 100)] 
    n_obs = 1000
    nb_modalities = 5
    df['feature'] = rd.choice(mod, size=n_obs)
    df['target'] = rd.choice([0, 1], size=n_obs, p=[0.9, 0.1])
    mymap = get_encoding(df, 'target', 'feature', nb_modalities=nb_modalities)
    assert len(set(mymap.values())) == nb_modalities, "nb of encoding shall be equal to nb_modalities"
    ##}


