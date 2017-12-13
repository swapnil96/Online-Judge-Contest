
n, x = map(int, raw_input().split())
a = map(int, raw_input().split())
ans = 0
temp = {}
for i in xrange(n):
    temp[a[i]] = 1

for i in xrange(x+1):
    if i in temp:
        if i == x:
            ans += 1

    else:
        if i == x:
            continue
        
        ans += 1

print ans
