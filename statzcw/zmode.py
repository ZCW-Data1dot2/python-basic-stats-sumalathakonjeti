from statzcw import zcount

def z_mode(list):
    list.sort()
    for i in range(len(list)):
        if i == 0:
            mode_value = list[i]
            mode_count = 1
            prev_mode_value = list[i]
            prev_mode_count = 0
        else:

            if mode_value == list[i]:
                mode_count = mode_count + 1
            else:
                # print(mode_value, mode_count, list[i],prev_mode_count,prev_mode_value)
                if mode_count > prev_mode_count:
                    prev_mode_count = mode_count
                    prev_mode_value = mode_value
                    mode_count = 1
                    mode_value = list[i]
                    # print(prev_mode_count,prev_mode_value)
                else:
                    mode_value = list[i]
                    mode_count = 1
    return prev_mode_value




# file_path = 'dataOne.csv'
# list_x = zcount.get_csv(file_path, 'x')
# z_mode(list_x)
# print(list_x)
