tt = int(raw_input())

for i in xrange(tt):

    n = int(raw_input())
    a = map(int, raw_input().split())

    a.sort()

    l = a[n: 2*n]

    ans = []

    for j in xrange(n):
        ans.append(a[j])
        ans.append(a[j+n])

    print l[n/2]

    print ' '.join(map(str, ans))    

    # print a,   l, ans