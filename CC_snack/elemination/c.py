
def find(a):

	tot = sum(a[2:])
	if (a[0]*a[1] < tot) or (a[0]*a[1] > tot):
		return 'No'

	x = a[2]
	y = a[3]
	z = a[4]
	remain1 = [x,y,z]
	remain2 = [z,x,y]
	remain3 = [y,z,x]
	remain4 = [x,z,y]
	remain5 = [z,y,x]
	remain6 = [y,x,z]
	r10 = a[0]
	r11 = a[1]
	while bool(remain1):
		got = 0
		for i in remain1:
			if i % r10 == 0:
				got = 1
				r11 -= i / r10
				k = i
				break

			elif i % r11 == 0:
				got = 1
				r10 -= i / r11
				k = i
				break

		if got == 0 or r10 <= 0 or r11 <= 0:
			break	
	
		remain1.remove(k)
		if len(remain1) == 1:
			if r10*r11 == remain1[0]:
				return 'Yes'

	if not bool(remain1):
		return 'Yes'		
	
	r20 = a[0]
	r21 = a[1]
	while bool(remain2):
		got = 0
		for i in remain2:
			if i % r20 == 0:
				got = 1
				r21 -= i / r20
				q = i
				break

			elif i % r21 == 0:
				got = 1
				r20 -= i / r21
				q = i
				break

		if got == 0 or r20 == 0 or r21 == 0:
			break

		remain2.remove(q)
		if len(remain2) == 1:
			if r20*r21 == remain2[0]:
				return 'Yes'

	if not bool(remain2):
		return 'Yes'	

	r30 = a[0]
	r31 = a[1]	
	while bool(remain3):
		got = 0
		for i in remain3:
			if i % r30 == 0:
				got = 1
				r31 -= i / r30
				w = i
				break

			elif i % r31 == 0:
				got = 1
				r30 -= i / r31
				w = i
				break
	
		if got == 0 or r30 == 0 or r31 == 0:
			break			

		remain3.remove(w)
		if len(remain3) == 1:
			if r31*r30 == remain3[0]:
				return 'Yes'

	if not bool(remain3):
		return 'Yes'

	r40 = a[0]
	r41 = a[1]
	while bool(remain4):
		got = 0
		for i in remain4:
			if i % r40 == 0:
				got = 1
				r41 -= i / r40
				q = i
				break

			elif i % r41 == 0:
				got = 1
				r40 -= i / r41
				q = i
				break

		if got == 0 or r40 == 0 or r41 == 0:
			break

		remain4.remove(q)
		if len(remain4) == 1:
			if r40*r41 == remain4[0]:
				return 'Yes'

	if not bool(remain4):
		return 'Yes'	
	
	r50 = a[0]
	r51 = a[1]
	while bool(remain5):
		got = 0
		for i in remain5:
			if i % r50 == 0:
				got = 1
				r51 -= i / r50
				q = i
				break

			elif i % r51 == 0:
				got = 1
				r50 -= i / r51
				q = i
				break

		if got == 0 or r50 == 0 or r51 == 0:
			break

		remain5.remove(q)
		if len(remain5) == 1:
			if r50*r51 == remain5[0]:
				return 'Yes'

	if not bool(remain5):
		return 'Yes'	

	r60 = a[0]
	r61 = a[1]
	while bool(remain6):
		got = 0
		for i in remain6:
			if i % r60 == 0:
				got = 1
				r61 -= i / r60
				q = i
				break

			elif i % r61 == 0:
				got = 1
				r60 -= i / r61
				q = i
				break

		if got == 0 or r60 == 0 or r61 == 0:
			break

		remain6.remove(q)
		if len(remain6) == 1:
			if r60*r61 == remain6[0]:
				return 'Yes'

	if not bool(remain6):
		return 'Yes'	

	return "No"		
			
sol = []
tt = int(raw_input())
for i in xrange(tt):
	a = map(long, raw_input().split())
	sol.append(find(a))

for i in xrange(tt):
	print sol[i]	

