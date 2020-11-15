from statzcw import zcount

def zmean1(list):
    mean1 = sum(list)/len(list)
    return round(mean1,3)


# file_path ='dataOne.csv'
# list_x = zcount.get_csv(file_path,'x')
# zmean1(list_x)


# def zmean():
#     l1,l2 = zcount.get_csv(x)
#     count_x = sum(l1)/len(l1)
#     count_y = sum(l2)/len(l1)
#     return (count_x,count_y)
#
# x = 'dataOne.csv'
#
# m1,m2 = zmean()
# print(m1)
# print(m2)