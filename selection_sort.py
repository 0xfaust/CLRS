#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Selection Sort'''

def selection_sort(a):
    for j in range(len(a)):
        min_index = j
        for i in range(j + 1, len(a)):
            if a[i] < a[min_index]:
                min_index = i
        a[j], a[min_index] = a[min_index], a[j]
    return a
        
a = [5, 2, 4, 6, 1, 3]

print(selection_sort(a))
