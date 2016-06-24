

a = map(int, raw_input().split())

if a[0] >= 7 and a[1] >= 7:
	print 0

elif a[0] >= 7 and a[1] < 7:
	tot = (6)*(a[1] - 1) - (a[1] - 1)
	print tot

elif a[0] < 7 and a[1] >= 7:
	tot = (6)*(a[0] - 1) - (a[0] - 1)

else:
	tot = a[0]*a[1] - min(a[0], a[1])
	print tot
		


