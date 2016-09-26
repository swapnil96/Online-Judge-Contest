
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

n, c = map(int, raw_input().split())
a = map(int, raw_input().split())
count = 1
for i in xrange(1, n):
	if (a[i] - a[i-1] <= c):
		#print a[i] - a[i-1]
		count += 1	

	else:
		count = 1

print count
