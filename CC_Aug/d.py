
tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	a = map(int, raw_input().split())
	s, e = map(int, raw_input().split())
	mini = 0
	curr = 0
	mini1 = 0
	curr1 = 0
	for j in xrange(s-1, e-1):
		curr += a[j]
		if j == e-2:
			continue

		if curr < mini:
			mini = curr

	for j in xrange(s-2, -1, -1):
		curr1 += a[j]
		if curr1 < mini1:
			mini1 = curr1

	#print 'adsf', curr1, mini1		
	for j in xrange(n-1, e-2, -1):
		curr1 += a[j]
		if j == e - 1:
			continue

		if curr1 < mini1:
			mini1 = curr1	

	#print curr, mini, curr1, mini1		
	'''
	if mini < 0 or mini1 < 0:
		temp = curr + mini1*2
		temp1 = curr1 + mini*2
		fin = min(temp, temp1)

	else:
		fin = min(curr, curr1)
	'''
	
	fin = min(curr, curr1, curr+(2*mini1), curr1+(2*mini))	
	print fin				