tt = int(raw_input())
for i in xrange(tt):
	u, v = map(int, raw_input().split())
	tot = (u+v)*(u+v+1)/2
	print tot+u+1
