
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

tt = int(raw_input())
a = raw_input()
count = 0
temp = []
for i in xrange(tt):
	if a[i] == 'B':
		count += 1

	else:
		if count != 0:
			temp.append(count)

		count = 0	

if a[tt - 1] == 'B':
	temp.append(count)

length = len(temp)
print length
if length != 0:
	print ' '.join(map(str, temp))

