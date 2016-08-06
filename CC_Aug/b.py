
#import time

tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	a = map(int, raw_input().split())
	tot = 0
	fin = set()
	for j in xrange(n):
		if j in fin:
			tot += 1
			continue
			
		nxt = a[j] + j + 1
		if nxt > n - 1:
			nxt = nxt % n

		vis = set()
		while True:
			if nxt == j:
				tot += 1
				fin = vis
				break
	
			nxt = a[nxt] + nxt + 1
			if nxt > n - 1:
				nxt = nxt % n

			if nxt in vis:
				break

			vis.add(nxt)	

	print tot

'''
import numpy
tt = int(raw_input())
for i in xrange(tt):
	n = int(raw_input())
	a = map(int, raw_input().split())
	arr = [[0 for _ in xrange(n)] for _ in xrange(n)]
	for j in xrange(n):
		to = j + a[j] + 1
		if to > n -1:
			to = to % n

		arr[j][to] = 1

	mat = numpy.matrix(arr)
	ans = 0
	fin = mat
	#print fin
	for k in xrange(n-1):
		fin = fin*mat
		#print fin
		tot = 0
		for j in xrange(n):
			if fin[j,j] == 1:
				tot += 1

		ans = max(tot, ans)		
		if ans == n:
			break
	
	print ans	

'''



