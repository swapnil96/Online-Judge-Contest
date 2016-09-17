
tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	a = []
	height = []
	growth = []
	for j in xrange(n):
		b = map(int, raw_input().split())
		height.append(b[0])
		growth.append(b[1])

	if height[0] > height[1]:
		prev = -1
		seq_h = -1

	else:
		prev = 1
		seq_h = 1

	if height[0] > height[1]:
		seq_g = -1

	else:
		seq_g = 1	

	is_h = 1
	is_g = 1
	print prev
	for j in xrange(1, n-1):
		diff1 = height[j] > height[j+1]
		diff2 = growth[j] > growth[j+1]
		if diff1 > 0:
			if prev == 1 and is_h == 1:
				prev = -1
			
			else:
				seq_h = -1
				is_h = 0				

		else:
			if prev == -1 and is_h == 1:
				prev = 1

			else:
				seq_h = -1
				is_h = 0

		if diff2 > 0:
			if prev == -1 and is_g == 1:
				seq_g = -1

			else:
				seq_g = -1
				is_g = 0

			nex = max(nex, (height[j] - height[j+1] + 0.0)/(growth[j+1] - growth[j]))		
		
		else:
			if prev == 1 and is_g == 1:
				seq_g = 1

			else:
				is_g = 0			
				seq_g = -1
	
	if is_g == 1 and is_h == 1:
		if seq_g == seq_h:
			print 1
			print 0, "INF"

		else:
			print 2
			print 0, ans
			print ans, "INF"	

	elif is_h == 1 and is_g == 0:
		print 1
		print 0, ans

	elif is_h == 0 and is_g == 1:
		print 1
		print  ans, 'INF'

	else:
		print 0	


