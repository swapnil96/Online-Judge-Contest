'''Link - https://www.codechef.com/problems/CHEFTET'''

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    b = map(int, raw_input().split())
    a = map(int, raw_input().split())
    s = sum(a) + sum(b)
    if n == 1:
        print s
        continue

    if s % n != 0:
        print -1
        continue

    ans = s / n
    for j in xrange(n):
        if j == 0:
            x = ans - a[j]
            if x == 0:
                pass

            elif x == b[j]:
                b[j] = 0

            elif x == b[j] + b[j + 1]:
                b[j] = 0
                b[j + 1] = 0

            elif x == b[j + 1]:
                b[j + 1] = 0

            else:
                ans = -1
                break

        elif j == n - 1:
            a[j] += b[j] + b[j - 1]
            if a[j] != ans:
                ans = -1
                break

        else:
            a[j] += b[j - 1]
            x = ans - a[j]
            if x == 0:
                b[j - 1] = 0

            elif x == b[j]:
                b[j] = 0

            elif x == b[j] + b[j + 1]:
                b[j] = 0
                b[j + 1] = 0

            elif x == b[j + 1]:
                b[j + 1] = 0

            else:
                ans = -1
                break

    print ans
