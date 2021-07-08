from statzcw import zcount,zmean
from math import sqrt

def correlation(listx,listy):
    sub_x =[]
    sub_y = []
    square_x =[]
    square_y = []
    ab =[]
    mean_x = zmean.zmean1(listx)
    mean_y = zmean.zmean1(listy)
    for i in range(len(listx)):
         a = listx[i] - mean_x
         sub_x.append(a)
         square_x.append(a ** 2)

    for i in range(len(listy)):
        b = listy[i] - mean_y
        sub_y.append(b)
        square_y.append(b ** 2)

    for i in range(len(listx)):
        ab.append(sub_x[i] * sub_y[i])

    sum_square_x = sum(square_x)
    sum_square_y = sum(square_y)
    sum_ab = sum(ab)
    corr = sum_ab/sqrt((sum_square_x)*(sum_square_y))
    return round(corr,5)



# file_path ='dataOne.csv'
# list_x = zcount.get_csv(file_path,'x')
# list_y = zcount.get_csv(file_path,'y')
#
# print(correlation(list_x,list_y))