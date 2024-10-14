# -*- coding: utf-8 -*-
"""CSE221_LAB-02_Task1(b).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17FAgYgpkM9EKgawYUK7DQ8BptzxBeuLX
"""

def find_sum_pair(n, s, arr):
    num_set = set()
    for i in range(n):
        complement = s - arr[i]
        if complement in num_set:
            return arr.index(complement) + 1, i + 1
        num_set.add(arr[i])
    return "IMPOSSIBLE"

with open("/content/Input1(b).txt", "r") as file:
    n, s = map(int, file.readline().split())
    arr = list(map(int, file.readline().split()))

result = find_sum_pair(n, s, arr)

with open("/content/Output1(b).txt", "w") as file:
    file.write(str(result))