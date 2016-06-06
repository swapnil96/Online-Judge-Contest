
def find(a, b):

	got0 = pro1 = pro0 = got1 = operation = 0
	if 1 in a:
		got1 = 1

	if 0 in a:
		got0 = 1

	for i in xrange(len(a)):
		if a[i] != b[i]:
			if a[i] == 1:
				pro1 += 1

			else:
				pro0 += 1	
		
		if pro1 >= 1 and pro0 >= 1:
			operation += 1
			pro0 -= 1
			pro1 -= 1
		
	#print pro0, pro1, got0, got1	
	if got0 == 1 and pro1 > 0:
		operation += pro1
		pro1 = 0

	if got1 == 1 and pro0 > 0:
		operation += pro0
		pro0 = 0		

	return operation		
					

tt = int(raw_input())
sol = []
for i in xrange(tt):
	a = map(int, list(raw_input()))
	b = map(int, list(raw_input()))
	sol.append(find(a, b))

for i in xrange(tt):
	if sol[i] == 0:
		print 'Unlucky Chef'

	else:
		print 'Lucky Chef'
		print sol[i]		