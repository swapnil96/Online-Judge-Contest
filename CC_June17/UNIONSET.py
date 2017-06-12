tt = int(raw_input())
for i in xrange(tt):
	n, kk = map(int, raw_input().split())
	data = []
	size = []
	for j in xrange(n):
		temp = map(int, raw_input().split())
		data.append(temp[1:])
		size.append(temp[0])

	contains = []
	for j in xrange(n):
		temp = {}
		for k in xrange(size[j]):
			temp[data[j][k]-1] = 1

		contains.append(temp)

	ans = 0
	for j in xrange(n):
		for k in xrange(j+1, n):
			if size[j] + size[k] < kk:
				continue

			flag = 0
			for l in xrange(kk):
				try:
					t = contains[j][l]
					
				except:
					try:
						t = contains[k][l]
					
					except:
						flag = 1
						break

			if flag == 0:
				ans += 1

	print ans