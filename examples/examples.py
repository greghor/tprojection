##{
from matplotlib import pyplot as plt
import pandas as pd
import pdb
from tprojection import Tprojection
from tprojection.datasets import load_data
##}


##{ use the titanic dataset for our examples
df = load_data("titanic")
target = "survived"
##}


##{ example of target and feature being both categorical. The confidence interval is estiamted by bootsrapping with 100 estimators
tproj = Tprojection(df, target, "sex", target_type="categorical", feature_type="categorical", n_estimators=100)
tproj.plot()
##}

##{ example of target and feature being  categorical and continuous, resp.
## note that I do not explicitely provide the type of variables here (categorical or continuous),
## it is infered by the class using a simple rule of thumb
tproj = Tprojection(df, target, "fare")
tproj.plot()
##}

##{ example of target and feature being both categorical. Here, we use a dummy encoding since the number of original features modalities is too high
tproj = Tprojection(df, target, "cabin", feature_type="categorical", nb_buckets=10, n_estimators=100)
tproj.plot()
print(tproj.encoding) # contains the mapping between the original modalities and the encoded modalities
##}

##{ example with target and feature being continuous and categorical, resp.
tproj = Tprojection(df, "fare", "cabin", feature_type="categorical", nb_buckets=10)
tproj.plot()
print(tproj.encoding) # contains the mapping between the original modalities and the encoded 
##}

##{ example with target and feature being both continuous. Not the most interesting 
# situation, since we use a simple scatter plot here.
tproj = Tprojection(df, "fare", "age", nb_buckets=10)
tproj.plot()
##}

