from statzcw import zstdev,zcount
from math import sqrt

def standard_error(list):
    x = zstdev.standard_dev(list)
    y = sqrt(len(list))
    return round(x/y ,5)

#
# file_path = 'dataOne.csv'
# list_x = zcount.get_csv(file_path, 'x')
# print("Standard Error",standard_error(list_x))