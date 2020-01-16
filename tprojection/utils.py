import pandas as pd
import numpy as np

def is_continuous(s, thresh):
    """
    Parameters
    ----------------

    c : pd series
        c is
    thresh : vartype
        thresh is

    Returns
    ----------------
    Boolean

    """
    try:
       _ = pd.to_numeric(s)
    except:
        return False
    if s.nunique()/s.count() < thresh:
        return False
    else:
        return True

##{ test with titanic dataset
feature = 'cabin'
df = load_data("titanic").fillna(value={feature: 'na'})
target = 'survived'
nb_modalities = 5
##}
def get_encoding(self, df, target, feature, nb_modalities):

    assert(nb_modalities < len(df[feature].unique()), "the number of encoded modalities shall be lower than the number of unique element in {}".format(self.feature))
    assert df[feature].isna() == 0, "feature column shall not contain missing value"
    dg = df.groupby(feature).agg({target: ["count", "mean"]})
    dg.columns = ["count", "mean"]
    dg["cumratio"] = dg["count"].cumsum()/dg["count"].sum()
    dg["ratio"] = dg["count"]/dg["count"].sum()

    # isolate modality with high frequency
    thresh_freq = 1/nb_modalities/2
    high_freq_modalities = list(dg[dg.ratio > thresh_freq].index)
    nb_high_freq_modalities = len(high_freq_modalities)
    high_freq_map = {v: v for v in high_freq_modalities}

    # regroup low frequency modalities
    low_freq_dg =  dg[dg.ratio <= thresh_freq]
    slicer = np.linspace(0, 1, nb_modalities + 1 - nb_high_freq_modalities)
    ii = 1
    mymap = {"g" + str(ii+1): [] for ii in range(nb_modalities)}
    for row in low_freq_dg.iterrows():
        if row[1]["cumratio"] > slicer[ii]:
            ii+=1
        mymap["g" + str(ii)].append(row[0])
    low_freq_map = {moda: k for k, vals in mymap.items() for moda in vals}

    return dict(high_freq_map, low_freq_map)


