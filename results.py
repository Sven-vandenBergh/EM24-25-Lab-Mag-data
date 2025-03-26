######################
#---Import-modules---#
######################

import numpy as np
from IPython.display import display

mu00 = []
######################
#---Results-a--------#
######################

#~ results a ~
B = 9.842857009521065e-05   #T
B_err = 6.655321996201567e-07   #T

I = 10.00   #A
I_err = 0.005   #A

r = 1.5*1e-2    #m
r_err = 0.1*1e-2    #m

mu0 = 2 * np.pi * r * B / I
mu0_err = 2 * np.pi * mu0 * np.sqrt( (r_err/r)**2 + (I_err/I)**2 + (B_err/B)**2 )
mu = (mu0, mu0_err)
print(f"a: {mu}")
mu00.append(mu0)

######################
#---Results-b--------#
######################

#~ results b ~
#B = (1.1630952380287918e-05 +/- 7.966214243964197e-08)*I + (-1.739285713864921e-05 +/- 5.490334290927476e-07)

gamma = 1.1630952380287918e-05
gamma_err = 7.966214243964197e-08

r = 1.5*1e-2    #m
r_err = 0.1*1e-2    #m

mu0 = 2 * np.pi * r * gamma
mu0_err = 2 * np.pi * mu0 * np.sqrt( (r_err/r)**2 + (gamma_err/gamma)**2 )
mu = (mu0, mu0_err)
print(f"b: {mu}")
mu00.append(mu0)

######################
#---Results-c--------#
######################

#~ results c ~
#B = (1.6879101846741345e-06 +/- 3.227987538699855e-08)/r + (-1.7465558130820592e-05 +/- 1.3882102122218266e-06)

epsilon = 1.6879101846741345e-06
epsilon_err = 3.227987538699855e-08

I = 10.00   #A
I_err = 0.005   #A

mu0 = 2 * np.pi * epsilon / I
mu0_err = 2 * np.pi * mu0 * np.sqrt( (epsilon_err/epsilon)**2 + (I_err/I)**2 )
mu = (mu0, mu0_err)
print(f"c: {mu}")
mu00.append(mu0)

mu00 = np.asarray(mu00)
mean_mu = mu00.mean(axis=0)
print(f"mean mu0: {mean_mu}")