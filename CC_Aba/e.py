'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

m, n = map(int, raw_input().split())
mod = 10**9 + 7

fac = [1]*(10**6 + 1)
for i in xrange(2, 10**6 + 1):
    fac[i] = fac[i-1] * i % mod

a = min(m, n)
b = max(m, n)

ans = 1
for i in xrange(2, a):
    ans = fac[i] * ans % mod

ans = ans * ans % mod

for i in xrange(b-a+1):
    ans = ans * fac[a] % mod

print ans
