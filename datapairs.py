import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os
import fnmatch
import re
import numpy as np
from parcel_function import parcel_counter as p_c


# Constants used throughout the program-----------------------------------------------------------------------
# Arrays for plots
Concentration = []
Time = []
# Region used
x_r = [-0.3, 0.3]
y_r = [1, 1.8]
z_r = [-2.65, 2.65]
volume = (abs(x_r[0]-x_r[1])*abs(y_r[0]-y_r[1])*abs(z_r[0]-z_r[1]))
# Constants used for concentration conversion. SET MANUALLY using Fluent simulation values
rho = 998.2  # kg/m^3, liquid water
p_aveD = 1E-7  # m
total_particles = 1.86547E15  # [-]
total_parcels = 438  # [-]
total_mass = 9.75E-4  # kg
mper_parcel = total_mass/total_parcels


# Get parcels using function and create data pair---------------------------------------------------------------
# Path where Ansys store .dpmrpt files for transient simulation
dirpath=r'C:\Users\andys\Desktop\CFD Covid\CRv2.0\CR_files\dp0\FLU\Fluent'

# Store only .dpmrpt files in list
dfiles=fnmatch.filter(os.listdir(dirpath), '*.dpmrpt')

# Loop through list and call p_c for each .dpmrpt file
for dfile in dfiles:

    # filepath for one dpmrpt file
    dfilepath=r'C:\Users\andys\Desktop\CFD Covid\CRv2.0\CR_files\dp0\FLU\Fluent\\' + dfile
    # get flowtime from file name. Note that findall returns a list of strings and we only want a float.
    flowtimes=re.findall("\d\.+\d\d", dfile)
    flowtime=float(flowtimes[0])
    # call p_c
    parcels = p_c(dfilepath, flowtimes[0], x_r, y_r, z_r)
    Concentration.append(parcels * mper_parcel)
    Time.append(flowtimes[0])

# Graph concentration vs time -------------------------------------------------------------------------------
Concentration = np.array(Concentration)
Time = np.array(Time)
print(Concentration)

fig, ax = plt.subplots()  # figure with axes
ax.plot(Time, Concentration)
ax.set_title('Concentration vs. Time')
ax.set_xlabel('Time [s]')  # Add an x-label to the axes.
ax.set_ylabel('Droplets concentration [kg/m^3]')  # Add a y-label to the axes.
plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.xaxis.set_ticks(np.arange(0, 110, 10))
plt.show()
