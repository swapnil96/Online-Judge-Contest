
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''


tt = int(raw_input())
a = list(raw_input())
#print a
count = 0
for i in xrange(1, tt-1):
	if a[i] == a[i-1]:
		#print a[i], a[i-1]
		if a[i] == a[i+1]:
			count += 1
			if a[i] == 'b':
				a[i] = 'r'

			else:
				a[i] = 'b'

		else:
			a[i], a[i+1] = a[i+1], a[i]
			count += 1

				
print count#, a