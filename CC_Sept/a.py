
tt = int(raw_input())
ans = []
for i in xrange(tt):
	a = raw_input()
	zeros = 0
	ones = 0
	c = len(a)
	for j in xrange(c):
		if a[j] == "0":
			zeros += 1

		else:
			ones += 1

	if (ones == 1)  or (zeros == 1):
		ans.append("Yes")

	else:
		ans.append("No")

for i in xrange(tt):
	print ans[i]		