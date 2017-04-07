'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    a = map(int, raw_input().split())
    h = [0]*(10**6)
    for j in xrange(n):
        h[a[j] - 1] += 1

    ans = 0
    for j in xrange(10**6):
        if (h[j] > 1):
            ans += h[j] * (h[j] - 1)

    print ans
