##{
from matplotlib import pyplot as plt
import pandas as pd
import pdb
from tprojection.tprojection import Tprojection
from tprojection.datasets import load_data
##}


##{ test with titanic dataset
df = load_data("titanic")
target = "survived"
##}

##{ example category to category plot with confidence interval inferred by bootsrapping with 100 estimators
tproj = Tprojection(df, target, "sex", target_type="categorical", feature_type="categorical", n_estimators=100)
tproj.plot()
##}

##{ example categortical to continuous
## note that I do not explicitely provide the type of variables here (categorical or continuous),
## it is infered by the class using a simple rule of thumb
tproj = Tprojection(df, target, "fare")
tproj.plot()
##}

##{ example of category to category where we use a dummy encoding since the number of original features modalities is too high
tproj = Tprojection(df, target, "cabin", feature_type="categorical", nb_modalities=5)
tproj.plot()
print(tproj.encoding) # contains the mapping between the original modalities and the encoded modalities
##}


