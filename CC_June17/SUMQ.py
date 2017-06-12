import bisect
mod = 10**9 + 7
tt = int(raw_input())
for i in xrange(tt):
	p, q, r = map(int, raw_input().split())
	a = map(int, raw_input().split())
	b = map(int, raw_input().split())
	c = map(int, raw_input().split())
	a.sort()
	b.sort()
	c.sort()

	s_a = [a[0]]
	s_c = [c[0]]
	for j in xrange(1, p):
		s_a.append(s_a[j-1]+a[j])

	for j in xrange(1, r):
		s_c.append(s_c[j-1]+c[j])

	tot = 0
	for j in xrange(q):
		idx1 = bisect.bisect(a, b[j])
		idx2 = bisect.bisect(c, b[j])
		if idx1 != 0 and idx2 != 0:
			tot += (b[j]*b[j]*(idx1)*(idx2))%mod
			tot += (b[j]*idx2*s_a[idx1-1])%mod
			tot += (b[j]*idx1*s_c[idx2-1])%mod
			tot += (s_a[idx1-1]*s_c[idx2-1])%mod

	print tot % mod
