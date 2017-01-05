'''Link - https://www.codechef.com/problems/FRJUMP'''

import math
modulo = 10**9 + 7

n = int(raw_input())
que = map(int, raw_input().split())
query = int(raw_input())
log = [0]
prod = [0]
divi = [[] for i in xrange(n)]
for i in xrange(1, n + 1):
    l = 0
    p = 1
    for j in xrange(i, n, i):
        l +=  math.log10(que[j])
        p = (p*que[j])%(modulo)
        divi[j].append(i)

    log.append(l)
    prod.append(p)

for i in xrange(query):
	a = map(int, raw_input().split())
	if a[0] == 1:
		r = a[1]
		if r == 1:
			que[0] = a[2]

		else:
			temp = pow(que[r-1], modulo - 2, modulo)
			for j in divi[r-1]:
				prod[j] = (prod[j]*a[2]*temp)%(10**9+7)
				log[j] += math.log10(a[2]) - math.log10(que[r-1])

			que[r-1] = a[2]

	else:
		x = log[a[1]] + math.log10(que[0]) - math.floor(log[a[1]] + math.log10(que[0]))
		s = str(math.pow(10,x))
		answer = (prod[a[1]]*que[0])%(modulo)
		print s[0],answer
