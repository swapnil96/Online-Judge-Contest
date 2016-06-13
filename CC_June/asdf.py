from numpy import *
import temp
from time import *
'''
tt = map(int, raw_input().split())
temp1 = []
for i in xrange(tt[0]):
	temp1.append(map(int, raw_input().split()))

que = array(temp1)
'''
que = array(temp.aol)
tt = [500, 500]
now = time()
sums = que.cumsum(axis = 0).cumsum(axis = 1)
print time() - now
then = time()
for i in xrange(5000):
	sum1 = que.max()

print time() - then