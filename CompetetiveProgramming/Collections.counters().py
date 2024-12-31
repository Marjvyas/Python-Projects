from collections import Counter
no_shoes=int(input())
shoe_sizes=[int(x) for x in input().split(' ')]
customer=int(input())
v=[]
result=0
count_shoe=Counter(shoe_sizes)
for x in range(customer):
    temp=[int(y) for y in input().split(' ')]
    v.append(temp)

for i in v:
    if i[0] in count_shoe.keys() and count_shoe[i[0]]!=0:
        result+=int(i[1])
        count_shoe[i[0]]-=1
print(result)
#use of counter
# >>> from collections import Counter
# >>>
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>>
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>>
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]
