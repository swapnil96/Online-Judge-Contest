

tt = int(raw_input())
for i in xrange(tt):
	a = map(int, raw_input().split())
	v = []
	for j in xrange(a[0]):
		v.append(map(int, (' '.join(n for n in raw_input())).split()))

	b = [sum(x) for x in zip(*v)]	
	ans = 0
	for i in xrange(a[1]):
		if b[i] > 1:
			g = b[i]
			ans += ((g)*(g - 1))/2

	print ans

		