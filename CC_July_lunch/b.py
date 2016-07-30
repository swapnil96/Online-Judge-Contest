t = int(raw_input())
for i in xrange(t):
	n, p, q = map(int, raw_input().split())
	a = map(int, raw_input().split())
	a.sort()
	fin = 0
	'''
	for j in xrange(n):
		if q > 0:
			if q*2 >= a[j]:
				if a[j] & 1 == 0:
					q -= a[j]/2
					a[j] = 0
					fin += 1

				else:
					q -= (a[j] - 1)/2
					a[j] = 1	

			else:
				a[j] -= q*2
				q = 0
				
		else:
			break

	for j in xrange(n):
		if a[j] == 0:
			continue

		if p > 0:
			if p >= a[j]:
				p -= a[j]
				a[j] = 0
				fin += 1

			else:
				a[j] -= p
				p = 0
				
		else:
			break

	print fin		
	'''
	tot = 0
	if p == 0:
		for j in xrange(n):
			if a[j]	& 1 == 0:
				if q*2 >= a[j]:
					tot += 1
					q -= a[j]/2

					
	if q == 0:

		for j in xrange(n):
			if p > 0:
				if p >= a[j]:
					p -= a[j]
					a[j] = 0
					tot += 1

				else:
					a[j] -= p
					p = 0
					
			else:
				break

	print tot			