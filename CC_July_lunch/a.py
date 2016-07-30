t = int(raw_input())
for i in xrange(t):
	n, k = map(int, raw_input().split())
	a = map(int, raw_input().split())
	v = [0 for j in xrange(n)]
	d = [0 for j in xrange(n)]
	for j in xrange(n):
		if a[j] == j + 1:
			d[j] = 1

		v[a[j]-1] += 1

	tot = 0	
	for j in xrange(n):
		if v[j]	>= k and d[j] == 0:
			tot += 1

	print tot		
