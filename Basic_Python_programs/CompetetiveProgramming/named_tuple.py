from collections import namedtuple
# use case:
# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.
#
# Example
#
# Code 01
#
# >>> from collections import namedtuple
# >>> Point = namedtuple('Point','x,y')
# >>> pt1 = Point(1,2)
# >>> pt2 = Point(3,4)
# >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# >>> print dot_product
# 11
# Code 02
#
# >>> from collections import namedtuple
# >>> Car = namedtuple('Car','Price Mileage Colour Class')
# >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# >>> print xyz
# Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# >>> print xyz.Class
# Y

# Sample Input
#
# TESTCASE 01
#
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
# TESTCASE 02
#
# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5
# Sample Output
#
# TESTCASE 01
#
# 78.00 <== AVG OF MARKS
# TESTCASE 02
#
# 81.00
N = int(input())
M = [x for x in (' '.join(input().split()).split(' '))]
# input().split() fun will convert the entered string into the list by removing the spaces between individual words
i = 1
marks = 0
while i <= 4:
    if M[i - 1] == 'MARKS':
        break
    else:
        i += 1
# cls=namedtuple('cls',' '.join(M))
for x in range(N):
    tup = (' '.join(input().split()).split(' ', i))
    if tup[i - 1].strip().isdigit():
        marks += int(tup[i - 1])

print(marks / N)
