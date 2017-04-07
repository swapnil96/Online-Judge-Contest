'''Link - https://www.codechef.com/problems/MSTEP'''

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    a = []
    for j in xrange(n):
        a.append(map(int, raw_input().split()))

    x = [-1]*(n**2)
    y = [-1]*(n**2)

    for j in xrange(n):
        for k in xrange(n):
            x[a[j][k]-1] = j
            y[a[j][k]-1] = k

    dist = 0
    for j in xrange(1, n*n):
        dist += abs(x[j] - x[j-1]) + abs(y[j] - y[j-1])

    print dist
