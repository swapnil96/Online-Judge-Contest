'''Link - https://www.codechef.com/problems/SUBINC'''

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    a = map(int, raw_input().split())
    j = 0
    k = 1
    count = n
    while j < n:
        now = a[j]
        while k < n:
            if a[k] >= now:
                now = a[k]

            else:
                break

            k += 1

        count += (k - j)*(k - j - 1)/2
        j = k
        k += 1

    print count
