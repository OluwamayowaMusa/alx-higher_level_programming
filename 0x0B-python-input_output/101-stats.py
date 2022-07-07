#!/usr/bin/python3
""" Reads standard input line by line and compute metrics """

file_size = []
status_dict = {}
i = 0
for line in open(0, 'r', encoding='utf-8'):
    try:
        i += 1
        temp = line.split()
        file_size.append(int(temp[-1]))
        if status_dict.get(int(temp[-2]), 0) == 0:
            status_dict[int(temp[-2])] = 1
        else:
            status_dict[int(temp[-2])] += 1
        if i % 10 == 0:
            print("File size: {}".format(sum(file_size)))
            for i in sorted(status_dict):
                print("{}: {}".format(i, status_dict[i]))
    except KeyboardInterrupt:
        break

print("File size: {}".format(sum(file_size)))
for i in sorted(status_dict):
    print("{}: {}".format(i, status_dict[i]))
