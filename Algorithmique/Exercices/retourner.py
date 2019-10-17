#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# longueur = len

# def decouper(string, pos):
#     return string[pos:]

# def retourner(value, pos):
#     l = longueur(value)
#     liste = list(value)
#     if pos < l // 2:
#         temp = liste[pos]
#         liste[pos] = value[l - pos - 1]
#         liste[l-pos-1] = temp
#         return retourner(''.join(liste), pos + 1)
#     return value

# print(retourner("Hello there", 0))


def inverse(string):
    if len(string) == 0:
        return string
    return inverse(string[1:]) + string[0]


print(inverse("Hello there"))