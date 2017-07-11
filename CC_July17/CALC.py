tt = int(raw_input())
for i in xrange(tt):
    n, b = map(int, raw_input().split())
    hi = n / b
    lo = 0
    ans = 0
    last = 0
    while lo <= hi:
        mid = (lo+hi)/2
        save = n - b*mid
        curr = save * mid
        if curr >= ans:
            lo = mid+1

        else: 
            hi = mid
        
        ans = max(ans, curr)
        if last == 1:
            break

        if lo == hi:
            last = 1


    print ans