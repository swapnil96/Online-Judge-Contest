'''Link - https://www.codechef.com/JAN17/problems/DIGITSEP'''

import fractions

tt = int(raw_input())
fin = []
for i in xrange(tt):
    n = int(raw_input())
    a = raw_input()
    m, x, y = map(int, raw_input().split())
    fromto = [[0 for _ in xrange(n)] for __ in xrange(n)]
    dp = [[{} for _ in xrange(n)] for __ in xrange(n)]
    for j in xrange(n):
        num = 0
        for k in xrange(j, n):
            num = (num * 10) + int(a[k])
            if len(str(num)) > m:
                while k < n:
                    fromto[j][k] = -1
                    k += 1

                break

            fromto[j][k] = num

    for j in xrange(y+1):

        for k in xrange(n):
            dp[j][k][0] = -1

    for j in xrange(n):

        if fromto[0][j] == -1:
            break

        dp[0][j][fromto[0][j]] = 1
        dp[0][j][0] = 0

    ans = 0
    for j in xrange(1, y+1):

        for k in xrange(n):

            for l in xrange(k+1, n):

                if fromto[k+1][l] != -1 and dp[j-1][k][0] != -1:
                    for m in dp[j-1][k].keys():
                        if m == 0:
                            continue

                        dp[j][l][fractions.gcd(m, fromto[k+1][l]) ] = 1
                        dp[j][l][0] = 0

        if n > 18:
            if j > (x + y)/2:
                break

        if j > x - 1:
            ans = max(ans, max(dp[j][n-1]))

    fin.append(ans)

for i in xrange(tt):
    print fin[i]
