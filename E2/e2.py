######################
#---Import-modules---#
######################

import os
from matplotlib.pyplot import figure, show, subplots
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.ticker import ScalarFormatter

def path_e2(filename):
    directory_pth = r"C:\Users\Gebruiker\Documents\Uni\EM LABS\MAG\E2"
    PATH = os.path.join(directory_pth, filename)
    return PATH

######################
#---Import-rdata-de--#
######################

#get path
file = "d_e_raw_data.csv"
PATH = path_e2(file)

#load raw data
rdata_de = pd.read_csv(PATH)
rdata_de.columns = rdata_de.columns.str.replace('"', '').str.strip()

print(rdata_de.columns)

#define z-axis
z = rdata_de['z (cm)']*1e-2
z_err = rdata_de['z_err (cm)']*1e-2


#define measurements for parallel case
Bp_mean = rdata_de[['B trial_1 (parallel mT)', 'B trial_2 (parallel mT)', 'B trial_3 (parallel mT)']].mean(axis=1)*1e-3
Bp_err = rdata_de[['B trial_1 (parallel mT)', 'B trial_2 (parallel mT)', 'B trial_3 (parallel mT)']].std(axis=1)*1e-3

#combined error parallel case
sigma1 = np.sqrt(z_err**2 + Bp_err**2)


#define measurements for anti-parallel case
Bap_mean = rdata_de[['B trial_1 (anti-parallel mT)', 'B trial_2 (anti-parallel mT)', 'B trial_3 (anti-parallel mT)']].mean(axis=1)*1e-3
Bap_err = rdata_de[['B trial_1 (anti-parallel mT)', 'B trial_2 (anti-parallel mT)', 'B trial_3 (anti-parallel mT)']].std(axis=1)*1e-3

#combined error anti-parallel case
sigma2 = np.sqrt(z_err**2 + Bap_err**2)


######################
#-----Plot-data------#
######################

fig = figure(tight_layout=True, figsize=(8,3))

#plot data d
ax = fig.add_subplot(1,2,1)
ax.errorbar(z, Bp_mean, xerr=z_err, yerr=Bp_err, fmt='o', color='darkslategrey',
            elinewidth=2, capsize=5, markerfacecolor='darkslategrey', markersize=8,
            label='parallel')     #parallel case

#grid and ticks
ax.grid(True, which='both', axis='both', linestyle='--', color='gray', alpha=0.5)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
ax.legend()


#plot data e
ax = fig.add_subplot(1,2,2)
ax.errorbar(z, Bap_mean, xerr=z_err, yerr=Bap_err, fmt='o', color='#4a728c',
            elinewidth=2, capsize=5, markerfacecolor='#4a728c', markersize=8,
            label='anti-parallel')     #anti-parallel case

#grid and ticks
ax.grid(True, which='both', axis='both', linestyle='--', color='gray', alpha=0.5)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
ax.legend()


fig.tight_layout()
show()