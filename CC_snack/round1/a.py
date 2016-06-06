import collections
import itertools

tt = int(raw_input())
sol = []
for i in xrange(tt):
	a = int(raw_input())
	b = map(int, raw_input().split())
	#c = collections.Counter(b)
	#if len(c) <= (a - 2):
	got = max(len(list(v)) for g,v in itertools.groupby(b)) 
	#print got
	if got >= 3:
		sol.append('Yes')

	else:
		sol.append('No')	
	#print c

for i in xrange(tt):
	print sol[i]
