
import time
from math import floor

MOD = 10**9 + 9
'''
prev_even = {}
prev_odd = {}

def find(no):

	if no & 1 == 0:
		if no in prev_even:
			return prev_even[no] % MOD
	
		if bool(prev_even):
			start = max(prev_even.keys())	
			ans = prev_even[start]

		else:
			#print 'adsf'
			start = 0
			ans = 0

		for i in xrange(start + 2, no+1, 2):
			c1 = pow(i, 2, MOD)
			ans += (4 * c1) - ((i-1)*6)
			prev_even[i] = ans
	
	else:
		if no in prev_odd:
			return prev_odd[no] % MOD
	
		if bool(prev_odd):
			start = max(prev_odd.keys())	
			ans = prev_odd[start]
		else:
			start = 1	
			ans = 1
	
		for i in xrange(start + 2, no+1, 2):
			c1 = pow(i, 2, MOD)
			ans += (4 * c1) - ((i-1)*6)
			prev_odd[i] = ans
	
	return ans % MOD		
'''

def find(no):

	if no & 1 == 0:
		i = no / 2
		return (((8*(i)*(i+1)*(2*i + 1))/3) - (6*i*(i+1)) + 6*i)

	i= int(floor(no/2))
	return (2*i*(8*i*i+15*i+13))/3+1

tt = int(raw_input())
for i in xrange(tt):
	a = int(raw_input())	
	#now = time.time()
	print find(a) % MOD
	#print time.time() - now

#print prev_even	