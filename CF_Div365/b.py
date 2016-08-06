
n, k = map(int, raw_input().split())
beu = map(int, raw_input().split())
cap = map(int, raw_input().split())
'''
tot = 0
for i in xrange(n-1):
	if (i + 1) in cap:
		for j in xrange(n):
			if j < i:
				if ((j + 1) in cap) or (j == i - 1) : 
					continue

				else:
					tot += beu[j]*beu[i]

			elif j > i:
				tot += beu[i]*beu[j]

	else:
		tot += beu[i]*beu[i+1]		
'''

tot1 = beu[0]*beu[n-1]
for i in xrange(n-1):
	tot1 += beu[i]*beu[i+1]

done = []
for j in cap:
	done.append(j - 1)
	for l in xrange(n):
		if l in done:
			continue

		if (l == j - 2) or (l == j):
			continue	

		if (j == 1 and l == n -1) or (j == n and l == 0):
			continue

		tot1 += beu[j-1]*beu[l]

print tot1

'''
if 1 in cap:
	pass

elif n in cap:
	pass

else:
	tot += beu[0]*beu[n-1]

print tot	
'''