
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
'''

tt = int(raw_input())
sol = []
for i in xrange(tt):
	a = map(int, raw_input().split())
	ones = a[0] + a[1] - 2
	tot = a[1]*a[0]
	twos = 2 * (tot - ones - 1)
	sol.append(twos + ones)

for i in xrange(tt):
	print sol[i]	