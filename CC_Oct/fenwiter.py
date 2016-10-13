'''Link - https://www.codechef.com/OCT16/problems/FENWITER'''

tt = int(raw_input())
for i in xrange(tt):
	a = raw_input().split()
	fre = int(a[3])
	found = -1
	ans = 0
	if found == -1:
		for j in xrange(len(a[2])-1, -1, -1):
			if a[2][j] == '0':
				found = j
				break

		if found != -1:
			for j in xrange(0, len(a[0])):
				if a[0][j] == '1':
					ans += 1
			
			temp = 0	
			for j in xrange(0, len(a[1])):
				if a[1][j] == '1':
					temp += 1	

			ans += temp*fre + 1
			
			for j in xrange(0, found+1):
				if a[2][j] == '1':
					ans += 1
					
	if found == -1:
		for j in xrange(len(a[1])-1, -1, -1):
			if a[1][j] == '0':
				found = j
				break

		if found != -1:
			for j in xrange(0, len(a[0])):
				if a[0][j] == '1':
					ans += 1
			
			temp = 1
			for j in xrange(0, found+1):
				if a[1][j] == '1':
					temp += 1	

			temp1 = 0
			for j in xrange(0, len(a[1])):
				if a[1][j] == '1':
					temp1 += 1	

			ans += temp1*(fre - 1) + temp			

	if found == -1:
		for j in xrange(len(a[0]) - 1, -1, -1):
			if a[0][j] == '0':
				found = j
				break

		if found != -1:
			for j in xrange(0, found+1):
				if a[0][j] == '1':
					ans += 1
			
			ans += 1

 	if found == -1:
 		ans = 1

	print ans	
