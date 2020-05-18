##{
import pandas as pd
from os.path import dirname
##}

def load_data(dataset):
    """
    load test dataset, possible options are:
    - titanic

    Parameters
    ----------------

    dataset : str
        required dataset

    Returns
    ----------------

    pandas  DataFrame
    """

    module_path = dirname(__file__)
    return pd.read_csv(module_path + "/{}.csv".format(dataset))


