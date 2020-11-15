from statzcw import zcount,zvariance
from math import sqrt

def standard_dev(list):
    x = zvariance.find_var(list)
    return round(sqrt(x),3)

#
# file_path = 'dataOne.csv'
# list_x = zcount.get_csv(file_path, 'x')
# print("Standard deviation",standard_dev(list_x))