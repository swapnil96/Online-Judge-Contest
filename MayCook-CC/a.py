'''Problem name - EZNO'''
'''It is related to polydivisible number and also Horner's rule is used'''

modulo = 10**9 + 7

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]


def find(b):

	base = b[0]
	length = b[1]
	i = 0
	got = 0

	while i >= 0:

		a = ''.join(map(str, numberToBase(i, base)))
		#print a, 'qewr'
		
		if len(a) < length:
			pass

		elif len(a) > length:
			break

		else:
			c = 1
			for j in xrange(1, length+1):
				#print a[:j]
				b = int(a[:j])
				#print b,'asdf'
				if b % j != 0:
					#print 'guyu'
					c = 0
					break

			if c == 1:
				got += 1

		i += 1

	return got % modulo

tt = int(raw_input())
sol = []
for i in xrange(tt):
	a = raw_input()
	b = map(int, a.split())
	sol.append(find(b))

for i in xrange(tt):
	
	print sol[i]	