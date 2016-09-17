
t = int(raw_input())
temp = [0]*(2**18)
for i in xrange(t):
	v = raw_input().split()
	if v[0] == '+':
		a = map(int, (' '.join(v[1])).split())
		num = ''
		for j in a:
			if j % 2 == 0:
				num += '0'

			else:
				num += '1'	

		temp[int(num, 2)] += 1

	elif v[0] == '-':
		a = map(int, (' '.join(v[1])).split())
		num = ''
		for j in a:
			if j % 2 == 0:
				num += '0'

			else:
				num += '1'	
	
		temp[int(num, 2)] -= 1

	else:
		g = int(v[1], 2)
		#print g
		print temp[g]	
			
