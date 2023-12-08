#!/usr/bin/env python3
import sys


def get_data():
    arr = ""
    for char in sys.stdin:
        arr += char
    arr = arr.split()
    return arr


if __name__ == '__main__':
    data_dict = {}
    no_modif = 1
    data = get_data()
    for i in range(2, len(data), 2):
        data_dict[data[i]] = 0
    for i in range(3, len(data), 2):
        if data[i] in data_dict.keys():
            data_dict[data[i]] += 1
    for key in data_dict.keys():
        if data_dict[key] == 0:
            print(key)
