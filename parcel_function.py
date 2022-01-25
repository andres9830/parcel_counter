# Made by AM 06/04/2021

# Test el pull request funciona 

import numpy as np

def parcel_counter(dfilepath, flowtime, x_region, y_region, z_region):
    """Show parcel count inside region delimited by coordinates provided by the user. All coordinates must
    be lists and flow time should be an integer in the form 000.000000. Your fluent files recorded in each macro
    should be called dvars-flowtime"""

    # Read file and store in list M, then array
    M = []
    with open(dfilepath,'r') as DPM_file:
        for i, line in enumerate(DPM_file):
            # dpmrpt files always begin at 18th line, so the first columns are ignored (19 works)
            if i > 19:
                a = [float(i) for i in line.split()]
                M.append(a)
    M = np.array(M)

    # Create array to store useful columns with coords
    M_coor = np.zeros([len(M), 4])
    M_coor[:, 1] = M[:, 1]
    M_coor[:, 2] = M[:, 2]
    M_coor[:, 3] = M[:, 3]
    for i in range(len(M)):
        M_coor[i, 0] = i + 1

    # Work with new array and check for particles enclosed within region
    R = []

    for i in range(len(M)):
        condition_x = M_coor[i, 1] > x_region[0] and M_coor[i, 1] < x_region[1]
        condition_y = M_coor[i, 2] > y_region[0] and M_coor[i, 2] < y_region[1]
        condition_z = M_coor[i, 3] > z_region[0] and M_coor[i, 3] < z_region[1]
        if condition_x and condition_y and condition_z:
            R.append(M_coor[i, :])
    R = np.array(R)
    parcel_count = len(R)

    return parcel_count
