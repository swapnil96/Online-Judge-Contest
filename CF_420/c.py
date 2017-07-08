n = int(raw_input())
lis = []
rem = 1
ans = 0
for i in xrange(2*n):
    a = raw_input().split()
    if a[0] == "add":
        temp = int(a[1])
        lis.append(temp)

    else:
        if len(lis) != 0:
            if lis[-1] == rem:
                lis.pop()
        
            else:
                ans += 1
                lis = []
        
        rem += 1

print ans