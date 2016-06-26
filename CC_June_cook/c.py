
import math

tt = int(raw_input())
for i in xrange(tt):
	h, s = map(int, raw_input().split())
	a = h**2 + 4*s
	b = math.sqrt(a)
	u = h**2 - 4*s
	if u < 0:
		print -1
		continue

	k = (b + math.sqrt(h**2 - 4*s))/2	
	m = b - k
	g = [h,k,m]
	g.sort()
	print ' '.join(map(str, g))