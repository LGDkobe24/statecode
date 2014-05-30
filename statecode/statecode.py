import re
import os
import csv
import pandas as pd
from copy import copy

pkg_dir, pkg_filename = os.path.split(__file__)
data_path = os.path.join(pkg_dir, "data", "statecode_data.csv")
data = pd.read_csv(data_path)

def statecode(codes=['Alabama', 'Arizona'], origin='state', target='abbreviation'):
    '''Convert to and US state names and abbreviations

    Parameters
    ----------

    codes : string or list of strings
        country names or country codes to convert
    origin : string
        'state' or 'abbreviation'
    target : string
        'state' or 'abbreviation'
    '''

    if type(codes) is not list:
        codes = [codes]
    if origin is 'state':
        origin = 'regex'

    ori = data[origin].tolist()
    tar = data[target].tolist()

    out = copy(codes)
    for i, v in enumerate(ori):
        out = [x if re.match('(?i)'+v, x) == None else tar[i] for x in out]

    return out
