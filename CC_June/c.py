
'''
pred = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
rem1 = {0: 8, 1: 0, 2: 2, 3: 4, 4: 4}
def last(n):

	q = str(n)
	w = ''
	for i in xrange(len(q), 01, -1):

		quo = n / 5**i
		rem = n % 5**i
		if quo >= 5:
			quo = n / 5**(i + 1)
			rem = n % 5**(i + 1)
	
		if rem == 0:
			w += str(rem1[quo])
			w += str(rem1[rem])
			n = rem
			continue
		
		w += str(pred[quo])		
		if rem < 5:
			w += str(rem1[rem])

		n = rem

	return w		

def find(n):

	k = 0
	#if n <= len(pred):
	#	return pred[n]
	#print 'asdf', len(pred)	
	for j in xrange(0, 10**12, 2):

		
		a = 0
		u = str(j)
		for p in u:
			if int(p) % 2 != 0:
				a = 1
				break

		if a == 1:
			continue
		
		k += 1
		#pred[k] = j
		if k == n:
			break

		
	return j				
'''

def base5(n):
    if n == 0: return
    for x in base5(n // 5): yield x
    yield n % 5

def seq(n):
    return int(''.join(str(2 * x) for x in base5(n)) or '0')

tt = int(raw_input())
sol1 = []
for l in xrange(tt):
	a = int(raw_input())
	sol1.append(seq(a-1))

for m in xrange(tt):
	print sol1[m]

#print pred		