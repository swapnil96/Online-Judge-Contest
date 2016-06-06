'''Wrong. HackerEarth. Problem name - Benny and interesting number'''
import math
def FindAllDivisors(x):
    divList = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    return divList

tt = int(raw_input())
sol = []
for i in xrange(tt):

    got = 0
    h = int(raw_input())
    r = list(set(FindAllDivisors(h)))
    print r
    for v in r:
        if v == h:
            continue

        if v == 1:
            got += 1

        if (len(list(set(FindAllDivisors(v)))) - 1) % 2 != 0:
            print FindAllDivisors(v)
            got += 1

    if len(r) == 1:
        sol.append('Yes')
        continue

    if got % 2 == 0:
        sol.append('No')

    else:
        sol.append('Yes') 

for i in xrange(tt):
    print sol[i]                