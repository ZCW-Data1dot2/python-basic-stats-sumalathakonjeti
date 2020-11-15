import csv
def get_csv(file_path,row_name):
    list1 = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list1.append(float(row[row_name]))
    return(list1)


def zcount1(list):

    count_x = len(list)
    return (count_x)




#file_path ='/Users/suma/PycharmProjects/pythonProject3/python-basic-stats-sumalathakonjeti/dataOne.csv'
file_path ='dataOne.csv'
# for i in range (2):
#     if i == 0:
#         row = 'x'
#     else:
#         row = 'y'
#     list = get_csv(file_path, row)
#     print(row)
#     print(zcount(list))
# list_x = get_csv(file_path,'x')
# print(zcount1(list_x))
# list_y = get_csv(file_path,'y')
# print(zcount1(list_y))



# import csv
# def get_csv(file_path,row_name):
#     list1 = []
#
#     with open(file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row_name == 'x':
#                 list1.append(float(row['x']))
#                 # list1.append(float(row[row_name]))
#             if row_name == 'y':
#                 list1.append(float(row['y']))
#     return(list1)
#
# file_path = '../dataOne.csv'
#
# print(get_csv(file_path,'x'))

