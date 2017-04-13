'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

n, m, k = map(int, raw_input().split())
a = map(int, raw_input().split())
inf = 10000
now = inf
idx = 0
for i in xrange(m, n):
    idx += 1
    if (a[i] <= k and a[i] != 0):
        now = 10 * idx
        break

now1 = inf
idx = 0
for i in xrange(m-2, -1, -1):
    idx += 1
    if (a[i] <= k and a[i] != 0):
        now1 = 10*idx
        break
        
print min(now, now1)        