tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	a = map(long, raw_input().split())
	ans = 0
	temp_m = 0
	size_m = 0
	temp_p = 0
	size_p = 0
	minus = []
	for j in xrange(n):
		if a[j] < 0:
			temp_m += a[j]
			size_m += 1
			minus.append(a[j])

		else:
			temp_p += a[j]
			size_p += 1

	ans = temp_p*size_p + temp_m
	minus.sort(reverse=True)
	for j in range(len(minus)):
		temp_p += minus[j]
		temp_m -= minus[j]
		size_p += 1
		ans = max(ans, temp_p*size_p+temp_m)
		
	print ans