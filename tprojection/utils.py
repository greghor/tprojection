import pandas as pd

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

