from itertools import combinations

# itertools.combinations(iterable, r)
# This tool returns the  length subsequences of elements from the input iterable.
#
# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
#
# Sample Code
#
# >>> from itertools import combinations
# >>>
# >>> print list(combinations('12345',2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
# >>>
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,4))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

# Sample Input
#
# HACK 2
# Sample Output
#
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

A,B=input().split()
A=sorted(A)
for i in range(1,int(B)+1):
    for j in combinations(A,i):
        print(''.join(j))