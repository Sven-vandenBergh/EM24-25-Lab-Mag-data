######################
#---Import-modules---#
######################

import os
from matplotlib.pyplot import figure, show, subplots
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.ticker import ScalarFormatter

def path_e3(filename):
    directory_pth = r"C:\Users\Gebruiker\Documents\Uni\EM LABS\MAG\E3"
    PATH = os.path.join(directory_pth, filename)
    return PATH

######################
#---Import-rdata-de--#
######################

#get path
file = "f_raw_data.csv"
PATH = path_e3(file)

#load raw data
rdata_f = pd.read_csv(PATH)
rdata_f.columns = rdata_f.columns.str.replace('"', '').str.strip()

