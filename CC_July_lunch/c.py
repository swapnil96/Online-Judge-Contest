import fractions
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

t = int(raw_input())
for i in xrange(t):
	n, k, l = map(int, raw_input().split())
	a = map(int, raw_input().split())
	g = set()
	for j in xrange(n):
		for k in xrange(n):
			g.add(fractions.gcd(a[j], a[k]))

	f = set(a)
	j = g - g.intersection(f)
	y = n - len(j)
	print nCr(y, k)