import math

tt = int(raw_input())
fin = []
for i in xrange(tt):
    m = int(raw_input())
    a = map(int, raw_input().split())
    a.sort()
    t = int(math.ceil(math.log(m, 2)))
    final = m
    ans = 0

    while(t > 0):
        temp = []
        for k in xrange(0, final-1, 2):
            l = (a[k] + a[k+1]) - 1
            ans += l
            # a[k/2] = l + 1
            temp.append(l+1)

        if (final % 2 != 0):
            # a[(final-1)/2] = a[final-1]
            temp.append(a[final-1])

        # a.sort()
        temp.sort()
        a = temp
        print a
        final = int(math.ceil(final/2.0))
        t -= 1

    fin.append(ans)

for i in xrange(tt):
    print fin[i]
