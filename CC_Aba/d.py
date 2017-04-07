'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

tt = int(raw_input())
for i in xrange(tt):
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())

    s = [0]*k
    for j in xrange(n):
        s[a[j]%k] += 1

    if s[0] == 0:
        ans = 0

    else:
        ans = 1

    if (k % 2 == 0):
        for j in xrange(1, k/2):
            ans += max(s[k - j], s[j])

        if s[k/2] >= 1:
            ans += 1

    else:
        for j in xrange(1, k/2 + 1):
            ans += max(s[k - j], s[j])

    print ans
