import string
import random
key=list(string.printable)
encode=list(string.printable)
random.shuffle(encode)
print(key)
print(encode)
mess=input("Enter your data which is to be encrypted:")
for i in mess:
    for j in key:
        if i==j:
            print(encode[key.index(j)], end='')