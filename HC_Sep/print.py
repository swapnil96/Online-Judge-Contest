'''Link - https://www.hackerearth.com/september-circuits/algorithm/print-hackerearth/'''

import collections

n = int(raw_input())
a = raw_input()
letters = collections.Counter(a)
h = letters['h'] / 2
a = letters['a'] / 2
c = letters['c']
k = letters['k']
e = letters['e'] / 2
r = letters['r'] / 2
t = letters['t']
print min(h, a, c, k, e, r, t)