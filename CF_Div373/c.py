
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

n, t = map(int, raw_input().split())
c = raw_input()
num = float(c)
b = list(c)
a = []
got = 0
for i in xrange(n):
	if b[i] == '.':
		got = 1
		ix = i
		continue

	a.append(int(b[i]))

carry = 0
if got == 1:
	k = n-3

else:
	k = n-2

idx = 10**9
get = 0
while (t > 0):	
	if t == 0:
			break

	t -= 1
	for i in xrange(ix, k):
		#print 'asdf'
		if a[i] == 9 and carry == 1:
			a[i] = 0

		else:
			a[i] += carry
			carry = 0	

		if a[i+1] >= 5:
			get = 1
			if a[i] == 9:
				a[i] = 0
				a[i+1] = 0
				carry = 1

			else:
				a[i] += 1
				a[i+1] = 0
			
			idx = min(idx, i)	

		else:
			pass

		#print a	
		if t <= 0:
			break

if carry == 1:
	a.insert(0, 1)
	ix += 1
	#print a

fin = ''
length = len(a)
if got == 1:
	if get == 1:
		for i in xrange(length):
				
			if i == ix:
				fin += '.'
			
				
			if i == idx:
				fin += str(a[i])
				break

				#fin += str(a[i]

			#else:
			fin += str(a[i])
			print i

	else:
		for i in xrange(length):
			#print 'asdfadsfads', get, got, length
			if i == ix:
				fin += '.'
				fin += str(a[i])

			else:
				fin += str(a[i])


else:
	if get == 1:
		for i in xrange(length):
			if i == idx:
				fin += str(a[i])
				break

			else:
				fin += str(a[i])	

	else:
		fin = c

print ('%f' % float(fin)).rstrip('0').rstrip('.')