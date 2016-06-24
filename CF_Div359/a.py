
import sys

'''
tt = int(raw_input().split())
a = map(int, raw_input().split())
a = map(int, (' '.join(n for n in raw_input())).split())
for i in xrange(tt):
'''
a = map(int, raw_input().split())
tot = a[1]
dis = 0
for i in xrange(a[0]):
	b = map(str, raw_input().split())
	if b[0] == '+':
		tot += int(b[1])

	else:
		if tot < int(b[1]):
			dis += 1

		else:
			tot -= int(b[1])		 

print tot, dis			
