'''link - https://www.codechef.com/OCT16/problems/CHEFKEY'''

from math import sqrt
def factors(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__, ([i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

tt = int(raw_input())
for i in xrange(tt):
	a = map(int, raw_input().split())
	fac = factors(a[2])
	#print fac
	count = 0
	for j in fac:
		width = j
		height = a[2]/j
		#print height, width
		if height <= a[0] and width <= a[1]:
			#print height, width
			if height == width:
				count += 1
				continue

			if width <= a[0] and height <= a[1]:
				count += 2

			else:
				count += 1

		elif height <= a[1] and width <= a[0]:
			#print height, width
			if height == width:
				count += 1
				continue

			if width <= a[1] and height <= a[0]:
				count += 2

			else:
				count += 1		
	
	print count					