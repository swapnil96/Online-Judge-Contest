'''Link - https://www.hackerearth.com/september-circuits/algorithm/fredo-and-large-numbers/'''

n = int(raw_input())
a = map(int, raw_input().split())
q = int(raw_input())
fre_ele = [1]*(n)
idx = sorted(range(n), key=a.__getitem__)
b = [i for i in a]
b.sort()
j = idx[0]
for i in xrange(1, n):
	if b[i-1] == b[i]:
		fre_ele[j] += 1
		fre_ele[idx[i]] = 0

	else:
		j = idx[i]
		
fre = [[] for _ in range(n)]	
big = [-1]*n		
fref = [-1]*n
for i in xrange(n):
	if fre_ele[i] != 0:
		fre[fre_ele[i]-1].append(a[i])

#print fre
fref[0] = fre_ele[0]
big[0] = a[0]
for i in xrange(1, n):
	fref[i] = max(fref[i-1], fre_ele[i])
	
	if fref[i-1] < fre_ele[i]:
		big[i] = a[i]

	else:
		big[i] = big[i-1]

#print fref
i = 0
fin = [0]*n
while i < n:

	if fref[i] == i:
		for k in xrange(i, n):
			fin[k] = 0

		break

	for j in xrange(i, fref[i]):
		fin[j] = big[i]

	i = fref[i]

#print big, fre, fin, big, fref
for i in xrange(q):
	que = map(long, raw_input().split())
	if que[0] == 0:
		print fin[que[1]-1]	

	else:
		if fre[que[1]-1] == []:
			print 0

		else:	
			print fre[que[1]-1][0]
		