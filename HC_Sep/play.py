'''Link - https://www.hackerearth.com/september-circuits/algorithm/mishki-playing-games/'''

import math

n, q = map(int, raw_input().split())
a = map(int, raw_input().split())
query = []
for i in xrange(q):
	query.append(map(int, raw_input().split()))

temp = [0]*n
temp[0] = int(math.log(a[0], 2)) + 1
for i in xrange(1, n):
	temp[i] = temp[i-1] + int(math.log(a[i], 2)) + 1

#print temp
for i in xrange(q):
	t = temp[query[i][1]-1] - temp[query[i][0]-1] + int(math.log(a[query[i][0] - 1], 2)) + 1
	#print t
	if (t % 2 != 0):
		print "Mishki"

	else:
		print "Hacker"	
