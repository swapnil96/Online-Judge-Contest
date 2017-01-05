'''Link - https://www.codechef.com/DEC16/problems/BASE'''

import math

def root(num, base):
    var = int(math.pow(num, 1.0/base))
    if (var+1)**base == num:
        return var + 1

    else:
        return var

tt = int(raw_input())
for i in xrange(tt):
    num = int(raw_input())
    if num == 0:
        print 0
        continue

    elif num == 1:
        print "INFINITY"
        continue

    half = num / 2
    if num & 1 == 0:
        count = half
    else:
        count = half + 1

    till = int(math.log(num, 2))
    for j in xrange(2, till+1):
        lar1 = root(num, j)
        lar2 = root(half, j)
        count += lar1 - lar2

    print count
