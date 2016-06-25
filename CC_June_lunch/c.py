
'''
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
'''

from math import sqrt    
def factors1(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

import fractions
def is_square(integer):
    root = sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def find(b, a):

	for i in xrange(a):
		v = factors1(b[i])
		got1 = 0
		for j in v:
			if j == 1:
				continue

			if is_square(j):
				got1 = 1
				ans = int(sqrt(j))

		if got1 == 1:
			break

	return ans		

def find1(b, a):
	got = 0
	for j in xrange(a):
		if is_square(b[j]):
			ans = int(sqrt(b[j]))
			got = 1
			break

		for k in xrange(j+1, a):
			fra = fractions.gcd(b[j], b[k])
			if fra != 1:
				ans = fra
				got = 1
				break

		if got == 1:
			break

	if got == 0:
		#print 'asdf'
		ans = find(b, a)

	return ans
		
tt = int(raw_input())
sol = []
que = []
for i in xrange(tt):
	a = int(raw_input())
	b = map(int, raw_input().split())
	que.append([b, a])

for i in xrange(tt):	
	sol.append(find1(que[i][0], que[i][1]))		

for i in xrange(tt):
	print sol[i]

#print factors1(48)
'''
for i in xrange(tt):
	a = int(raw_input())
	b = map(int, raw_input().split())
	pro = 1
	got = 0
	for j in xrange(a):
		pro *= b[j]
		g = factors1(pro)
		for k in g:
			if k == 1:
				continue

			if is_square(k):
				ans = int(sqrt(k))
				gpt = 1
				break

		if got == 1:
			break		

	print ans		
'''
#print factors1(49), is_square(49)