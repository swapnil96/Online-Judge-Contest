
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

tt = int(raw_input())
a = map(int, raw_input().split())

if tt == 1:
	if a[0] == 0:
		print "UP"

	elif a[0] == 15:
		print "DOWN"

	else:	
		print -1

else:
	#for i in xrange(tt):
	if a[tt-1] > a[tt-2]:
		if a[tt-1] == 15:
			print "DOWN"

		else:	
			print "UP"

	else:
		if a[tt-1] == 0:
			print "UP"

		else:	
			print "DOWN"	

