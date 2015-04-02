# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:35:40 2015

@author: joris
"""

import os
import pandas as pd


def read_file(filename):
    _, fname = os.path.split(filename)
    station = fname[:7]
    colnames = ['date'] + [item for pair in zip(["{:02d}".format(i) for i in range(24)], ['flag']*24) for item in pair]
    data = pd.read_csv(filename, sep='\t', header=None, index_col=['date'],
                       na_values=[-999, -9999], names=colnames)

    # for now, drop the flags
    data = data.drop('flag', axis=1)

    data = data.stack()
    data = data.reset_index(name=station)
    data.index = pd.to_datetime(data['date'] + ' ' + data['level_1'])
    data = data.drop(['date', 'level_1'], axis=1)

    return data


def load_data():


    #os.chdir("/data/Scipy/PyData Paris 2015/2015-PyData-Paris-pandas-intro")

    files = ["data/BETR8010000800100hour.1-1-1990.31-12-2012",
             "data/BETN0290000800100hour.1-1-1990.31-12-2012",
             "data/FR040370000800100hour.1-1-1999.31-12-2012",
             "data/FR040120000800100hour.1-1-1999.31-12-2012"]

    data = []

    for fname in files:
        df = read_file(fname)
        data.append(df)

    data = pd.concat(data, axis=1)

    return data
