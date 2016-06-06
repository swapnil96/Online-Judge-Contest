import numpy
#import temp
from operator import mul

n = int(raw_input())
que = map(int, raw_input().split())
#que = temp.lis
query = int(raw_input())
#print que

def find(no):

	pro = 1
	#temp = numpy.array(que[0::no])
	temp = que[0::no]
	#print temp, temp.prod()
	return (reduce(mul, temp))
	#return numpy.prod(temp, dtype=numpy.uint64)
	'''
	for i in xrange(0, n, no):
		#print i
		pro *= que[i]

	return pro	
	'''

modulo = 10**9 + 7
sol = []
k = 0
for i in xrange(query):
	a = map(int, raw_input().split())
	if a[0] == 1:
		que[a[1] - 1] = a[2]

	else:
		k += 1
		sol.append(find(a[1]))

for i in xrange(k):
	print str(sol[i])[0], int(sol[i] % modulo)
