#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Bubble Sort'''

def bubble_sort(a):
    for i in range(0, len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a
        
a = [5, 2, 4, 6, 1, 3]

print(bubble_sort(a))
