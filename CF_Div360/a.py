
import sys

'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

n, d  = map(int, raw_input().split())
ans = 0
maxi = -1
for i in xrange(d):
	a = map(int, (' '.join(n for n in raw_input())).split())
	if a.count(0) > 0:
		ans += 1

	else:
		ans = 0	

	if ans > maxi:
		maxi = ans	

print maxi