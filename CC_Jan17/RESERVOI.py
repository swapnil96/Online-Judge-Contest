'''Link - https://www.codechef.com/JAN17/problems/RESERVOI'''

tt = int(raw_input())
for i in xrange(tt):
    n, m = map(int, raw_input().split())
    mat = []
    for j in xrange(n):
        a = raw_input()
        temp = []
        for k in xrange(m):
            temp.append(a[k])

        mat.append(temp)

    ans = "yes"
    got = 0

    for j in xrange(n-1):

        for k in xrange(m-1):

            if k == 0:
                if mat[j][k] == "W":
                    ans = "no"
                    got = 1
                    break

            if k == m - 2:
                if mat[j][k+1] == "W":
                    ans = "no"
                    got = 1
                    break

            if mat[j][k] == "B":
                if mat[j+1][k] == "W" or mat[j+1][k] == "A":
                    ans = "no"
                    got = 1
                    break

            elif mat[j][k] == "W":
                if mat[j+1][k] == "A":
                    ans = "no"
                    got = 1
                    break

                if mat[j][k+1] == "A":
                    ans = "no"
                    got = 1
                    break

            else:
                if mat[j][k+1] == "W":
                    ans = "no"
                    got = 1
                    break

        if got == 1:
            break

    for j in xrange(m):
        if j == 0:
            if mat[n-1][j] == "W":
                ans = "no"
                break

        if j == m-1:
            if mat[n-1][j] == "W":
                ans = "no"
                break

            continue

        if mat[n-1][j] == "W":
            if mat[n-1][j+1] == "A":
                ans = "no"
                break

        elif mat[n-1][j+1] == "A":
            if mat[n-1][j+1] == "W":
                ans = "no"
                break

    for j in xrange(n):
        if j == n-1:
            if mat[j][m-1] == "W":
                ans = "no"
                break

            continue    

        if mat[j][m-1] == "W":
            ans = "no"
            break

        elif mat[j][m-1] == "B":
            if mat[j+1][m-1] == "W" or mat[j+1][m-1] == "A":
                ans = "no"
                break

    print ans
