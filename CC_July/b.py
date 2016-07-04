
def find(a, b, n):

	maxi = 0
	ans = 0
	if a[0] == 1:
		initial = 1

	else:
		initial = -1	

	for i in xrange(1, n):
		c = b[i] - b[i - 1]
		if c > maxi:
			maxi = c

		if a[i] == 1:
			if initial == 1:
				ans += c - maxi

			else:	
				ans += c
				initial = 1

			maxi = 0

		else:	
			ans += c		

		#print c, maxi, ans	
	return ans		

tt = int(raw_input())
sol = []
for i in xrange(tt):
	n = int(raw_input())
	a = map(int, (' '.join(n for n in raw_input())).split())
	b = map(int, raw_input().split())
	sol.append(find(a, b, n))

for i in xrange(tt):
	print sol[i]	

