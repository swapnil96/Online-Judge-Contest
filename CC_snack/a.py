


tt = int(raw_input())
sol = []
for i in xrange(tt):
	a = int(raw_input())
	b = map(int, raw_input().split())
	c = map(int, raw_input().split())
	got = 0
	for j in xrange(a):
		if j == 0:
			if b[0] >= c[0]:
				got += 1

		if (b[j] - b[j-1]) >= c[j]:
				got += 1

	sol.append(got)

for i in xrange(tt):

	print sol[i]				
		