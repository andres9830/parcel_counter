import numpy as np

def parcel_counter(x_region, y_region, z_region):
    """Show parcel count inside region delimited by coordinates provided by the user. All coordinates must
    be lists"""

    # Read file and store in list M, then array
    M = []
    with open(r'C:\Users\andys\Desktop\CFD Covid\CRv2.0\CR_files\dp0\FLU\Fluent\file.dpmrpt') as DPM_file:
        for i, line in enumerate(DPM_file):
            if i > 19:
                a = [float(i) for i in line.split()]
                M.append(a)
    M = np.array(M)

    # Create array to store useful columns with coords
    M_coor = np.zeros([365, 4])
    M_coor[:, 1] = M[:, 1]
    M_coor[:, 2] = M[:, 2]
    M_coor[:, 3] = M[:, 3]
    for i in range(365):
        M_coor[i, 0] = i + 1

    # Work with new array and check for particles enclosed within region
    R = []

    """
    Test values. DO NOT UNCOMMENT
    x_value = [-0.3, 0.3]  # Particles within person's width coordinates (use simmetry)
    y_value = [1, 1.8]  # Table Height taken as threshold value
    z_value = [-2.65, -2]  # Distance from mouth to center of table (greater than 1m required by social distancing)
    """

    for i in range(365):
        condition_x = M_coor[i, 1] > x_region[0] and M_coor[i, 1] < x_region[1]
        condition_y = M_coor[i, 2] > y_region[0] and M_coor[i, 2] < y_region[1]
        condition_z = M_coor[i, 3] > z_region[0] and M_coor[i, 3] < z_region[1]
        if condition_x and condition_y and condition_z:
            R.append(M_coor[i, :])
    R = np.array(R)
    parcel_count=len(R)
    return parcel_count

