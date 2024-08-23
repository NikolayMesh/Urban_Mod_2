my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
coun = 0
while coun <= len(my_list):
    if my_list[coun] > 0:
        print(my_list[coun])
    elif my_list[coun] == 0:
        coun += 1
        continue
    else:
        break
    coun += 1