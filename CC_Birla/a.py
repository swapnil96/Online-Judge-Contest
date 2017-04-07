n, k = map(int, raw_input().split())

a = map(int, raw_input().split())

ans = 0
fin = []

for i in xrange(n-1):
    if a[i] < 0:
        ans += 1
        a[i+1] = -1*a[i+1]
        fin.append(i+1)

if a[n-1] < 0:
    ans += 1
    fin.append(n)

print ans
if ans != 0:
    print ' '.join(map(str, fin))
