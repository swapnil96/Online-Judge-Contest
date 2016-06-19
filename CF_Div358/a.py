

tt = map(int, raw_input().split())
count = 0
for i in xrange(1, tt[0]+1):
	div = i / 5
	get = 5*(div+1) - i
	fin = tt[1] - get	
	count += fin / 5 + 1
		#print i, j

print count