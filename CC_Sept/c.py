
tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	a = []
	for j in xrange(n):
		a.append(map(int, raw_input().split()))

	high = -1
	for j in xrange(n):
		temp = a[j][0]
		count = [0]*6
		for k in xrange(1, temp + 1):
			count[a[j][k] - 1] += 1	
		
		while True:
			c = 0
			mini = 101
			for l in xrange(6):
				if count[l] > 0:
					if count[l] < mini:
						mini = count[l]

					c += 1

			if c == 4:
				count = [m - mini for m in count]
				temp += mini

			elif c == 5:
				count = [m - mini for m in count]
				temp += 2*mini

			elif c == 6:
				count = [m - mini for m in count]				
				temp += 4*mini
			
			else:
				break			

		if temp == high:
			res = "tie"

		elif temp > high:
			high = temp		
			res = "win"
			idx = j + 1

	if res == "tie":
		print "tie"

	else:	
		if idx == 1:		
			print "chef"

		else:
			print idx 	