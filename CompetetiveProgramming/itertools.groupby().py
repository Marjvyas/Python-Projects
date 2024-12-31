from itertools import groupby
# Sample Input
#
# 1222311
# Sample Output
#
# (1, 1) (3, 2) (1, 3) (2, 1)
A=input()
group=groupby(A)
for i,j in group:
    print((len(tuple(j)),int(i)), end=' ')
