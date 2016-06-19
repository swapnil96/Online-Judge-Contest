
def primes(n):
    divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
    return [ d for d in divisors if all( d % od != 0 for od in divisors if od != d ) ]

def find(a, b):

	g = []
	temp = []
	for i in xrange(a):
		o = [(j) for k in prev[b[i]] for j in temp if k == j]
		#print o
		if bool(o):
			continue

		if b[i] not in g:
			g.append(b[i])
			temp += prev[b[i]]
		#print temp, 'adsf', g

	#if b.count(1) > 1:
		extra = b.count(1) - 1

	#else:
	extra = 0	

	return len(g) + extra

prev = {}
for i in xrange(1, 10**3 + 1):
	prev[i] = primes(i)
	if not bool(prev[i]):
		prev[i].append(i)	

tt = int(raw_input())
sol = []
for i in xrange(tt):
	a = int(raw_input())
	b = map(int, raw_input().split())
	sol.append(find(a, b))

for x in xrange(tt):
	print sol[x]

	
