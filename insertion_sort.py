#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Insertion Sort'''

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A
        
A = [5, 2, 4, 6, 1, 3]

print(insertionSort(A))
