'''Link - https://www.codechef.com/problems/CAKECUT'''

def Xored(m, x, y):

    oo = 0
    tt = 0
    for i in xrange(1, m + 1):
        if x[i]^y[i] == 1:
            oo += 1

        else:
            tt += 1

    return (oo, tt + 1)

n, m = map(int, raw_input().split())
cum_xor = [[0 for _ in xrange(m + 1)] for __ in xrange(n + 1)]
mat = []
for i in xrange(n):
	b = map(int, (' '.join(n for n in raw_input())).split())
	mat.append(b)

for i in xrange(1, n  + 1):

    for j in xrange(1, m  + 1):

        cum_xor[i][j] = mat[i - 1][j - 1]
        cum_xor[i][j] ^= cum_xor[i - 1][j]
        cum_xor[i][j] ^= cum_xor[i][j - 1]
        cum_xor[i][j] ^= cum_xor[i - 1][j - 1]

ans = 0
for i in xrange(1, n + 1):

    for j in xrange(0, i):

        one, two = Xored(m, cum_xor[i], cum_xor[j])
        ans += one*(one - 1)/2
        ans += two*(two - 1)/2

print ans
