'''Link - https://www.codechef.com/OCT16/problems/CHDOGS'''

tt = int(raw_input())
for i in xrange(tt):
	a = map(int, raw_input().split())
	print '{0:.10f}'.format(2*(a[0])/(3.0 * a[1]))
