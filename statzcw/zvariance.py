from statzcw import zcount,zmean

def find_var(list):
    list1 = []
    x = zmean.zmean1(list)
    # print(x)
    for i in range(len(list)):
        var1 = list[i]
        var1 = float( var1 - x )
        var2 = var1 ** 2
        # var = float((float((list1[i]-x)) ** 2))
        list1.append(var2)
    var1 = sum(list1) / len(list1)
    return round(var1,3)


# file_path = 'dataOne.csv'
# list_x = zcount.get_csv(file_path, 'x')
# find_var(list_x)
#print("variance",find_var(list_x))
