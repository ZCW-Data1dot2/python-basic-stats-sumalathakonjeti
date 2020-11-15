import zcount1
import zmean1 ,zmed


#file_path ='/Users/suma/PycharmProjects/pythonProject3/python-basic-stats-sumalathakonjeti/dataOne.csv'
file_path ='dataOne.csv'

list_x = zcount1.get_csv(file_path,'x')
print(zcount1.zcount1(list_x))
list_y = zcount1.get_csv(file_path,'y')
print(zcount1.zcount1(list_y))
print(zmean1.zmean1(list_x))
print("median x", zmed.zmedian(list_x))


# for i in range (2):
#     if i == 0:
#         row = 'x'
#     else:
#         row = 'y'
#     list = get_csv(file_path, row)
#     print(row)
#     print(zcount(list))