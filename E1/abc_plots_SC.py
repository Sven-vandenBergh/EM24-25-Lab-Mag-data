######################
#---Import-modules---#
######################

import os
from matplotlib.pyplot import figure, show
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.ticker import ScalarFormatter

def path_e1(filename):
    """Returns the path of a given file in predefined directory."""
    directory_pth = r"C:\Users\Gebruiker\Documents\Uni\EM LABS\MAG\E1"
    path = os.path.join(directory_pth, filename)
    return path


######################
#---Import-rdata-a---#
######################

#get path
file = "a_raw_data.csv"
PATH = path_e1(file)

rdata_a = pd.read_csv(PATH)     #import raw data for experiment a

#define x-axis
x = rdata_a['x (cm)']*1e-2
x_err = rdata_a['x_error (cm)']*1e-2
print(x)

#get mean and std for each row
Ba_mean = rdata_a[['B trial_1 (mT)', 'B trial_2 (mT)', 'B trial_3 (mT)']].mean(axis=1)*1e-3
Ba_err = rdata_a[['B trial_1 (mT)', 'B trial_2 (mT)', 'B trial_3 (mT)']].std(axis=1)*1e-3

sigma = np.sqrt(x_err**2 + Ba_err**2)

def data(x, beta):
    """Return constant beta using scipy.optimize.curve_fit"""
    return beta

#fit data
beta, pcov = curve_fit(data, x, Ba_mean, sigma=sigma)
beta = beta[0]; beta_err = np.sqrt(pcov[0][0])

print("~ results a ~")
print(f"B = {beta} +/- {beta_err}\n")


######################
#---Import-rdata-b---#
######################

#get path
file = "b_raw_data.csv"
PATH = path_e1(file)

rdata_b = pd.read_csv(PATH)     #import raw data for experiment a

#omit quotes
rdata_b.columns = rdata_b.columns.str.replace('"', '').str.strip()

#define data points
I = rdata_b['I (A)']
I_err = rdata_b['I_err (A)']

Bb_mean = rdata_b[['B trial_1 (mT)', 'B trial_2 (mT)', 'B trial_3 (mT)']].mean(axis=1)*1e-3
Bb_err = rdata_b[['B trial_1 (mT)', 'B trial_2 (mT)', 'B trial_3 (mT)']].std(axis=1)*1e-3

sigma = np.sqrt(I_err**2 + Bb_err**2)

def datb(I, gamma0, gamma1):
    """Return constants gamma using scipy.optimize.curve_fit"""
    return gamma0 + gamma1 * I

gamma, pcov = curve_fit(datb, I, Bb_mean, sigma=sigma, p0=(-0.015, 0.005))
gamma0, gamma1 = gamma[0], gamma[1]
gamma0_err, gamma1_err= np.sqrt(pcov[0][0]), np.sqrt(pcov[1][1])

print("~ results b ~")
print(f"B = ({gamma1} +/- {gamma1_err})*I + ({gamma0} +/- {gamma0_err})\n")


######################
#---Import-rdata-c---#
######################

#get path
file = "c_raw_data.csv"
PATH = path_e1(file)

rdata_c = pd.read_csv(PATH)     #import raw data for experiment a

#omit quotes
rdata_c.columns = rdata_c.columns.str.replace('"', '').str.strip()

#define data points
r = rdata_c['d (cm)']*1e-2
r_err = rdata_c['d_err (cm)']*1e-2

Bc_mean = rdata_c[['B trial_1 (mT)', 'B trial_2 (mT)', 'B trial_3 (mT)']].mean(axis=1)*1e-3
Bc_err = rdata_c[['B trial_1 (mT)', 'B trial_2 (mT)', 'B trial_3 (mT)']].std(axis=1)*1e-3

sigma = np.sqrt(r_err**2 + Bc_err**2)

def datc(r, epsilon0, epsilon1):
    """Return constants epsilon using scipy.optimize.curve_fit"""
    return epsilon0 + epsilon1/r

epsilon, pcov = curve_fit(datc, r, Bc_mean, sigma=sigma)
epsilon0, epsilon1 = epsilon[0], epsilon[1]
epsilon0_err, epsilon1_err = np.sqrt(pcov[0][0]), np.sqrt(pcov[1][1])

print("~ results c ~")
print(f"B = ({epsilon1} +/- {epsilon1_err})/r + ({epsilon0} +/- {epsilon0_err})\n")


######################
#-----Plot-data------#
######################

#create plot
fig = figure(figsize = (10,9))

#plot data a
ax1 = fig.add_subplot(3,1,1)
ax1.errorbar(x, Ba_mean, xerr=x_err, yerr=Ba_err, fmt='o', color='#4a728c',
            elinewidth=2, capsize=5, markerfacecolor='#4a728c', markersize=8,
            label='$B_{mean}$')

#plot best fit
ax1.hlines(beta, np.asarray(x)[0], np.asarray(x)[-1], color='#4a728c', linestyle="--", label=f'Best fit:\n B = {beta:.3g} +/- {beta_err:.1g}')

#label axes
ax1.set_xlabel('x (m)', fontsize=14)
ax1.set_ylabel('$B_{mean}$ (T)', fontsize=14)
ax1.set_title('Magnetic Field Strength along Wire', fontsize=16)

#grid and ticks
ax1.grid(True, which='both', axis='both', linestyle='--', color='gray', alpha=0.5)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
ax1.legend()


#plot data b
ax2 = fig.add_subplot(3,1,2)
ax2.errorbar(I, Bb_mean, xerr=I_err, yerr=Bb_err, fmt='o', color='#4a8c76',
            elinewidth=2, capsize=5, markerfacecolor='#4a8c76', markersize=8,
            label='$B_{mean}$')

#plot best fit
ax2.plot(I, datb(I, gamma0, gamma1), color='#4a8c76', linestyle="--", label=f'Best fit:\n B = {gamma1:.3g}I + {gamma0:.3g}')

#label axes
ax2.set_xlabel('I (A)', fontsize=14)
ax2.set_ylabel('$B_{mean}$ (T)', fontsize=14)
ax2.set_title('Magnetic Field Strength vs. Current', fontsize=16)

#grid and ticks
ax2.grid(True, which='both', axis='both', linestyle='--', color='gray', alpha=0.5)
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
ax2.legend()


#plot data c
ax3 = fig.add_subplot(3,1,3)
ax3.errorbar(r, Bc_mean, xerr=r_err, yerr=Bc_err, fmt='o', color='darkslategrey',
            elinewidth=2, capsize=5, markerfacecolor='darkslategray', markersize=8,
            label='$B_{mean}$')

#plot best fit
ax3.plot(r, datc(r, epsilon0, epsilon1), color='darkslategrey', linestyle="--", label=f'Best fit:\n B = {epsilon1:.3g}/r + {epsilon0:.3g}')

#label axes
ax3.set_xlabel('r (m)', fontsize=14)
ax3.set_ylabel('$B_{mean}$ (T)', fontsize=14)
ax3.set_title('Magnetic Field Strength vs. Distance from Wire', fontsize=16)

#grid and ticks
ax3.grid(True, which='both', axis='both', linestyle='--', color='gray', alpha=0.5)
ax3.tick_params(axis='both', which='major', labelsize=12)
ax3.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax3.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
ax3.legend()

fig.subplots_adjust(hspace=0.4)
fig.tight_layout()
show()
