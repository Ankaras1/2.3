my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
m = 0
while m < len(my_list):
    if my_list[m] < 0:
        break
    elif my_list[m] == 0:
        m += 1
        continue
    elif my_list[m] > 0:
        print(my_list[m])
        m += 1













