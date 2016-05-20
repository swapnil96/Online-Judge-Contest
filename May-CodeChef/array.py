import itertools
def find(b):

	no = b[0]
	lim = b[1]

	lis = range(1, lim+1)
	
	a = list(itertools.product(*lis))
	print a
	







tt = int(raw_input())
sol = []
for i in xrange(tt):

	a = raw_input()
	b = map(int, a.split())
	(find(b))