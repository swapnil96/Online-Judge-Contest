import collections

n, k, p = map(int, raw_input().split())
aa = map(int, raw_input().split())
s = raw_input()

k = min(k, n)

a = []
for i in xrange(2*n):
    a.append(aa[i % n])

temp = []
ans = 0
for i in xrange(k):
    ans += a[i]

temp.append(ans)
for i in xrange(k, 2*n):
    ans -= a[i-k]
    ans += a[i]
    temp.append(ans)

temp.reverse()
d = collections.deque()

ans = []
size = n - k + 1
tot = 0
for i in xrange(size):

    while (tot != 0 and temp[i] >= temp[d[tot-1]]):
        d.pop()
        tot -= 1

    d.append(i)
    tot += 1

tot = len(d)
for i in xrange(size, len(temp)):
    
    ans.append(temp[d[0]])
    while (tot != 0 and d[0] <= i - size):
        d.popleft()
        tot -= 1
    
    while (tot != 0 and temp[i] >= temp[d[tot-1]]):
        d.pop()
        tot -= 1
    
    d.append(i)
    tot += 1
    
idx = 0
for i in xrange(len(s)):
    if s[i] == "?":
        print ans[idx % n]
    
    else:
        idx += 1
        