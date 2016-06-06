'''Problem name - P1Z2S'''

'''
Correct solution
n = int(raw_input())
a = raw_input()
b = map(int,a.split())
s = sum(b)

if s%2:
    print max(n,s/2+1)

else:
    print max(n,s/2)
''' 


a = int(raw_input())
b = raw_input()
c = map(int, b.split())
c.sort()
carry = 0
v = 0
i = 0
then = 0
while True:

	if i == a or sum(c) == 0:
		
		#print c, v, 'asd'
		now = c.count(0)
		if (now - then) == 0:
			v += a - now

		else:	
			v += (a - then)
		#print v
		then = now
		i = 0

	if sum(c) == 0:
		break	

	if c[i] == 0:
		#print 'asdf'
		i += 1
		continue

	if c[i] == 1:
		#print c, v
		c[i] = 0
		carry += 1
		i += 1
		continue

	c[i] -= 2

	if c[i] != 0:

		if c[i] < carry:
			c[i] = 0
			carry -= c[i]

		else:	 
			c[i] -= carry
			carry = 0

	i += 1
	
print v	