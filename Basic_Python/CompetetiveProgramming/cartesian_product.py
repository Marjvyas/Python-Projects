from itertools import product
A=(int(x) for x in input().split(' '))
B=(int(x) for x in input().split(' '))
ans=list(product(set(A),set(B)))
for i in ans:
    print(i, end=' ')