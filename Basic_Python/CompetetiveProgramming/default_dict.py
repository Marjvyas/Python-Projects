from collections import defaultdict
n,m=input().split(' ')
d=defaultdict(list)
# taking input for A word set
for i in range(int(n)):
    a=input().strip()
    d[a].append(i+1)

# taking input for B word set
for i in range(int(m)):
    b=input().strip()
    if b in d:
        print(''.join(str(x) for x in d[b]))
    else:
        print(-1)
# use of default dic:

# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print i
# This prints:
# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])