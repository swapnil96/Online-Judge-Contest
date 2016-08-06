
tt = int(raw_input())
for i in xrange(tt):
	n, m = map(int, raw_input().split())
	tot = n*m
	if tot & 1 == 0:
		print 'Yes'

	else:
		print 'No'	