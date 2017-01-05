'''Link - https://www.codechef.com/LTIME38/problems/LUMPYBUS'''

tt = int(raw_input())
for i in xrange(tt):
    n, p, q = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()
    ans = 0
    for i in xrange(n):
        x = min(q, a[i]/2)
        q -= x
        a[i] -= 2*x
        y = min(p, a[i])
        p -= y
        a[i] -= y
        if (a[i] == 0):
            ans += 1

        else:
            q += x
            p += y

    print ans
