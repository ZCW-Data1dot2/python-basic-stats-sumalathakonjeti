from statzcw import zcount


def zmedian(list):

    len1 = len(list)
    list.sort()
    if len1 % 2 == 0:
        median1 = list[len1/2]
        median2 = list[len1/2 - 1]
        median = median1 + median2
        print(median)

    else:
        median = list[(int(len1/2) + 1)]
        return (median)

# file_path = 'dataOne.csv'
# list_x = zcount.get_csv(file_path, 'x')
# print(zmedian(list_x))