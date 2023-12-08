#!/usr/bin/env python 3
import sys

def get_args():
    str = ""
    for char in sys.stdin:
        str += char
    return str

if __name__ == '__main__':
    str = get_args()
    x = str.splitlines()
    first = x[0].split()
    second = x[1].split()
    first_res = (int(first[3]) + int(first[2])) * int(first[1])
    second_res = (int(second[3]) + int(second[2])) * int(second[1])
    if first_res > second_res:
        print(second[0])
        exit(0)
    if second_res > first_res:
        print(first[0])
        exit(0)
