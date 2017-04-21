n = int(raw_input())

a = map(int, raw_input().split())

idx = 0
ans = 0
while idx < n - 2:

    if a[idx] % 2 == 0 and a[idx+1] % 2 == 0 and a[idx+2] % 2 == 0:
        ans += 0
        # idx += 1

    elif a[idx] % 2 == 0 and a[idx+1] % 2 == 0 and a[idx+2] % 2 != 0:
        ans += 0
        # idx += 1
    
    elif a[idx] % 2 == 0 and a[idx+1] % 2 != 0 and a[idx+2] % 2 == 0:
        ans += 2
        a[idx+1] = 2
        # idx += 2

    elif a[idx] % 2 == 0 and a[idx+1] % 2 != 0 and a[idx+2] % 2 != 0:
        ans += 1
        a[idx+1] = 2
        a[idx+2] = 2
        # idx += 3
    
    elif a[idx] % 2 != 0 and a[idx+1] % 2 == 0 and a[idx+2] % 2 == 0:
        ans += 2
        a[idx] = 2
        # idx += 2
    
    elif a[idx] % 2 != 0 and a[idx+1] % 2 == 0 and a[idx+2] % 2 != 0:
        ans += 2
        a[idx] = 2
        # a[idx+2] = 2

    elif a[idx] % 2 != 0 and a[idx+1] % 2 != 0 and a[idx+2] % 2 == 0:
        ans += 1
        a[idx] = 2
        a[idx+1] = 2        
    
    else:
        ans += 3
    
    idx += 1

if n == 2:
    if a[0] % 2 == 0 and a[1] % 2 == 0:
        ans = 0
    
    elif a[0] % 2 == 0 and a[1] % 2 != 0:
        ans = 2
    
    elif a[0] % 2 != 0 and a[1] % 2 == 0:
        ans = 2
    
    else:
        ans = 1
    
    
print "YES"
print ans
    
    

    
    
