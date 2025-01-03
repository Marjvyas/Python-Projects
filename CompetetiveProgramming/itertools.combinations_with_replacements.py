# itertools.combinations_with_replacement(iterable, r)
# This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
#
# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
#
# Sample Code
#
# >>> from itertools import combinations_with_replacement
# >>>
# >>> print list(combinations_with_replacement('12345',2))
# [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
# >>>
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,2))
# [(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]

# Sample Input
#
# HACK 2
# Sample Output
#
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

from itertools import combinations_with_replacement
A,B=input().split()
A=sorted(A)
for i in range(int(B),int(B)+1):
    for j in combinations_with_replacement(A,i):
        print(''.join(j))