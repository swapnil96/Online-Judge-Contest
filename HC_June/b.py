

tt =  int(raw_input())
sol = []
for i in xrange(tt):
	a = map(int, raw_input().split())
	b = list(map(int, raw_input().split()))
	sum1 = sum(b)
	#print sum1
	#print a, b, sum1
	if (sum1 + a[1])/(a[0] + 1)	< a[2]:
		sol.append("Impossible")
	
	else:
		#(sum1 + a[1])/(a[0] + 1) >= a[2]
		if a[2]*(a[0] + 1) - sum1 <= 0:
			sol.append(1)
		
		else:	
			sol.append(a[2]*(a[0] + 1) - sum1)

#print sol
for i in xrange(tt):
	print sol[i]