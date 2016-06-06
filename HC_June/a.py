p = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

sol = []
t = int(raw_input())
for i in xrange(t):
	a = list(raw_input())
	b = a.index('$')
	g = ''
	got = 0
	for j in a[b:]:
		if got == 1:
			if j not in p:
				if j == ' ':
					pass
				else:	
					break 

		if j in p:
			g += j
			got = 1

	sol.append('$%d'% int(g))
for i in xrange(t):
	print sol[i]