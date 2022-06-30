#!/usr/bin/python3
import sys


def func_diagonal_sum(list_1, list_2):
    for i in list_2:
        if sum(list_1) == sum(i):
            return 1
    return 0


def func_row(list_1, list_2):
    for i in list_2:
        if list_1[0] == i[0]:
            return 1
    return 0


def func_col(list_1, list_2):
    for i in list_2:
        if list_1[1] == i[1]:
            return 1
    return 0


def func_diagonal_sub(list_1, list_2):
    diff_1 = list_1[0] - list_1[1]
    for i in list_2:
        if diff_1 == (i[0] - i[1]):
            return 1
    return 0


def check_list(my_list, num):
    for index, temp in enumerate(my_list[::-1]):
        if temp[1] != num - 1:
            return index, temp
    return 0


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

for _c in sys.argv[1]:
    _i = ord(_c)
    if _i < 48 or _i > 57:
        print("N must be a number")
        sys.exit(1)
_num = int(sys.argv[1])
if _num < 4:
    print("N must be at least 4")
    sys.exit(1)
all_list = []
for i in range(_num):
    temp_1 = []
    for j in range(_num):
        temp_2 = []
        temp_2.append(i)
        temp_2.append(j)
        temp_1.append(temp_2)
    all_list.append(temp_1)

ctrl_1 = 0
j = 0
i = 1
result_list = []
result_list.append(all_list[j][ctrl_1])
while ctrl_1 < len(all_list):
    while j < len(all_list[ctrl_1]):
        if False:
            pass
        else:
            length_1 = len(result_list)
            temp_4 = all_list[i][j]
            if func_diagonal_sum(temp_4, result_list) == 1:
                j += 1
                if j == len(all_list[ctrl_1]):
                    i += 1
                    if i == len(all_list):
                        break
                    j = 0
                continue
            elif func_row(temp_4, result_list) == 1:
                j += 1
                if j == len(all_list[ctrl_1]):
                    i += 1
                    if i == len(all_list):
                        break
                    j = 0
                continue
            elif func_col(temp_4, result_list) == 1:
                j += 1
                if j == len(all_list[ctrl_1]):
                    i += 1
                    if i == len(all_list):
                        break
                    j = 0
                continue
            elif func_diagonal_sub(temp_4, result_list) == 1:
                j += 1
                if j == len(all_list[ctrl_1]):
                    i += 1
                    if i == len(all_list):
                        break
                    j = 0
                continue
            result_list.append(temp_4)
            if len(result_list) == _num:
                print(result_list)
            i += 1
            if i == len(all_list):
                break
            j = 0
    if check_list(result_list[1:], _num) != 0:
        ctrl_2, temp_1 = (check_list(result_list[1:], _num))
        i = temp_1[0]
        j = temp_1[1] + 1
        result_list[-(ctrl_2 + 1):] = []
    else:
        ctrl_1 += 1
        if ctrl_1 == len(all_list):
            break
        j = 0
        i = 1
        result_list = []
        result_list.append(all_list[j][ctrl_1])
