#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Linear Search'''

def linear_search(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return i
    return None
        
a = [5, 2, 4, 6, 1, 3]
v = 6

print(linear_search(a, v))
