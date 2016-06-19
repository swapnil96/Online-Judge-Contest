
def find(a):
	
	if a[0] % 2 != 0 and (a[1]*2 % a[0] != 0):
		return 'No'

	if a[1] % (a[0] / 2) != 0:
		return 'No'

	c = (2*a[1])/a[0]
	d = (a[0] - 1)
	if c <= d:
		return 'No'

	if c - d == 1:
		return 'No'

	if d == 2:
		if a[1] % 2 != 0:
			return 'No'

		if a[1] / 2 == 1:
			return 'No'

	for i in xrange(1, a[1]):
		divi = c - (d*i)
		if divi < 0:
			return 'No'

		if divi & 1 == 0 and divi != 0:
			return 'Yes'

tt = int(raw_input())
sol = []
for i in xrange(tt):
	a = map(int, raw_input().split())
	sol.append(find(a))

for i in xrange(tt):
	print sol[i]
	