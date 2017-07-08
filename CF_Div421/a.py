c, v0, v1, a, l = map(int, raw_input().split())
if a == 0:
    last_inc = 1

else:
    last_inc = (v1 - v0)/a + 1

ans = 0
for i in xrange(last_inc):
    today = v0 + i*a
    if i != 0:
        c -= today - l
    
    else:
        c -= today

    ans += 1
    # print c, 'adsf'
    if c <= 0:
        break

if c <= 0:
    print ans

else:
    # print 'fff'
    while True:
        if a == 0:
            c -= v0 - l
        
        else:
            c -= v1 - l

        ans += 1
        if c <= 0:
            break
    
    print ans
    