
n = int(raw_input())
c1, c2 = map(int, raw_input().split())
mat = []
for i in xrange(n):
	mat.append(map(int, raw_input().split()))

if c1 != 0:
	count1 = 0
	cost1 = 0
	count2 = 0
	cost2 = 0
	table1 = []
	table2 = []
	if c2 == 0:
		for i in xrange(n):
			for j in xrange(i+1, n):
				cost1 += mat[i][j]
			
			table1.append(i+1)
			count1 += 1

	else:
		for i in xrange(n):
			temp1 = 0
			temp2 = 0
			for j in table1:
				temp1 += mat[i][j-1]

			for j in table2:
				temp2 += mat[i][j-1]

			if temp1 <= temp2:
				if count1 < c1:
					table1.append(i+1)
					count1 += 1

				else:
					table2.append(i+1)	
					count2 += 1

			else:
				if count2 < c2:
					table2.append(i+1)			
					count2 += 1		

				else:
					table1.append(i+1)
					count1 += 1	

	print count1
	print ' '.join(map(str, table1))
					
else:
	print 0
	print 0