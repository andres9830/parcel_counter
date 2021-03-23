from coords import parcel_counter as p_c
parcels=p_c([-0.3, 0.3],[1, 1.8], [-2.65,-2])
print('There are {0} parcels in the desired region'.format(parcels))