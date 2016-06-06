

a = map(int, raw_input().split())
t = map(int, raw_input().split())
sol = []
if a[0] == 1:
	for i in xrange(a[1]):
		b = int(raw_input())
		if b == t[0]:
			sol.append("Yes")

		else:
			sol.append("No")

else:
	mi = min(t)
	ma = max(t)
	for i in xrange(a[1]):
		b = int(raw_input())
		if b > ma or b < mi:
			sol.append("No")

		else:
			sol.append("Yes")

for i in xrange(a[1]):
	print sol[i]

