import numpy as np
from scipy.constants import mu_0
from matplotlib.pyplot import figure, show

#define parameters
I = np.linspace(0,10,100)
r = (mu_0*I/np.pi)*10**4
r_cm = 100*r

B = "$B = B_{earth}$"

#plot figure
fig = figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(I, r_cm, color='darkslategrey')     #plot relation
ax.fill_between([0,10], [0, 4], 0, facecolor='cadetblue',
                alpha=0.45, label='Useful Measurement Range') #plot useful measurement range

ax.grid(True)
ax.set_xlabel("I (A)")
ax.set_ylabel("r (cm)")
ax.set_title(f"Distance (r) vs. Current (I), where {B}")
ax.legend()
show()