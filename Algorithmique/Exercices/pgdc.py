#!/usr/bin/python
# -*- coding: utf-8 -*-
 
def pgcd(a, b):
    if b == 0:
        return a
    r = a % b
    return pgcd(b, r)

print(pgcd(14, 87))