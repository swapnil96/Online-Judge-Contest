
a = raw_input()
temp = [0]*4
for i in xrange(len(a)):
	if a[i] == "R":
		temp[0] += 1

	elif a[i] == "L":
		temp[1] += 1

	elif a[i] == "U":
		temp[2] += 1

	else:
		temp[3] += 1			

if (len(a) % 2 != 0):
	print -1

else:
	g = abs(temp[0] - temp[1])
	h = abs(temp[2] - temp[3])
	ct = min(g, h)
	ct += (max(g, h) - ct)/2
	print ct