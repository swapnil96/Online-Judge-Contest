
tt = int(raw_input())
ans = []
for i in xrange(tt):
	a = raw_input()
	c = len(a)
	out  = ""
	cant = 0
	for j in xrange(int(c/2.0)):
		if (a[j] == "."):
			if(a[c - j - 1] == "."):	
				out += "a"	

			else:
				out += a[c - j - 1]

		elif (a[c - j - 1] == "."):
			out += a[j]

		else:
			if a[j] == a[c - j - 1]:
				out += a[j]

			else:
				cant = 1
				break	

	if cant == 1:
		ans.append(-1)
		continue

	if c & 1 == 1:
		if a[int(c/2.0)] == ".":
			ans.append(out + "a" + out[::-1])

		else:
			ans.append(out + a[int(c/2.0)] + out[::-1])	

	else:	
		ans.append(out + out[::-1])
			
for i in xrange(tt):
	print ans[i]