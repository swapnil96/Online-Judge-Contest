'''Link - https://www.codechef.com/problems/SQNUMBF'''

from fractions import gcd
import math

def root(num, base):
    var = int(math.pow(num, 1.0/base))
    if (var+1)**base == num:
        return var + 1

    else:
        return var

def solve(n, a):

    for i in xrange(n):
        for j in xrange(i + 1, n):
            g = gcd(a[i], a[j])
            if g > 1:
                return g

    for i in xrange(n):
        x = a[i]
        for j in xrange(1, root(x, 3)):
            if ( j > 1 and x % (j*j) == 0):
                return j

            if (x % j == 0):
                p = x / j
                t = root(p, 2)
                if (t > 1 and t*t == p):
                    return t

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    a = map(int, raw_input().split())
    print solve(n, a)
