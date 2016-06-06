

a = map(int, raw_input().split())
b = list(map(int, raw_input().split()))
'''
time = 0
i = 0
sum1 = 0
remain = a[1]
while True:

	for j in xrange(i, a[0]):
		if sum1 > remain:
			sum1 -= b[j-1]
			break

		if sum1 == remain:
			break

		sum1 = sum1 + b[j]

	print 'asdf', j, sum1
	while True:

		sum1 -= a[2]
		remain = a[1] - sum1
		time += 1
		break

	print remain, sum1		
	i = j - 1

	if j == a[0] - 1:
		break

print time, 'adsfasdf'
'''
time = 1
sum1 = 0
remain = a[1]
j = 0
while True:
	'''
	if sum1 < 0:
		sum1 = b[j]
		remain = a[1]
		
	'''		
	if remain >= b[j]:	
		for i in xrange(j, a[0]):
			sum1 += b[i]
			if sum1 > a[1]:
				j = i
				sum1 -= b[i]
				break

			if sum1 == a[1]:
				i += 1
				j = i
				remain = 0
				break	
	
	#print sum1, j, remain		
			

	sum1 -= a[2]
	time += 1
	remain = a[1] - sum1
	if j == a[0]:
		break
	#print remain, sum1, time, 'asdf'	

print time			










