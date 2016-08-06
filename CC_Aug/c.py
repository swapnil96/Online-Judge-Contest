
import numpy

n = int(raw_input())
a = []
for i in xrange(n):
	a.append(map(int, raw_input().split()))

array = numpy.matrix(a)
q = int(raw_input())
for i in xrange(q):
	k, x = map(int, raw_input().split())
	h = array**(k)
	tot = 0
	fin = []
	for j in xrange(n):
		if h[x-1,j] > 0: 
			tot += 1
			fin.append(j+1)

	if tot == 0:
		print 0
		print -1

	else:			
		print tot
		print ' '.join(map(str, fin))		
