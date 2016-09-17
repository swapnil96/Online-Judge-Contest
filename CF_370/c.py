
x, y = map(int, raw_input().split())
a = [y, y, y]
tot = 0
got = 0
while True:
	for i in xrange(3):
		a[i] = a[(i + 1)%3] + a[(i + 2)%3] - 1
		#print a[i], a[(i+1)%3], a[(i+2)%3]
		if a[i] > x:
			a[i] = x

		tot += 1	
		if (a[0] == a[1] and a[1] == a[2] and a[2] == x):
			got = 1
			break	
		
	if got == 1:
		break

print tot