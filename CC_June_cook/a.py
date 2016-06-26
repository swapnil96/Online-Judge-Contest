
import numpy

def matrixRegionSum2(A, D):
	#if len(que) == 0:
	#	return
	
	if A[0] == 0 or A[1] == 0: 
		OA = 0 

	else: 
		OA = sums[A[0]-1][A[1]-1]   

	if A[1] == 0: 
		OC = 0 

	else:
		OC = sums[D[0]][A[1]-1]   

	if A[0] == 0: 
		OB = 0 

	else: 
		OB = sums[A[0]-1][D[1]]   

	OD = sums[D[0]][D[1]]   

	return OD-OB-OC+OA

n, m = map(int, raw_input().split())
a = numpy.zeros(shape=(n, m))
for i in xrange(n):
	b = map(int, (' '.join(n for n in raw_input())).split())
	a[i] = b

sums = a.cumsum(axis = 0).cumsum(axis = 1)

#print a
#print sums
ans = 0
for i in xrange(n):
	for j in xrange(m):
		for k in xrange(1, n+ 1):
			for l in xrange(1, m + 1):
				if i + k > n:
					break

				if 	j + l > m:
					break

				sum1 = matrixRegionSum2([i, j], [i + k - 1, j + l - 1])
				#print sum1, i, j, k, l
				if int(sum1) & 1 == 0:
					ans += 1

print int(ans), matrixRegionSum2([0,0],[0,2]), sums					