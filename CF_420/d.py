n, k = map(int, raw_input().split())
start = []
end = []
off = []
for i in xrange(n):
    a, b, c = map(int, raw_input().split())
    start.append(a)
    end.append(b)
    off.append(c)

ans = 1
height = 0
j = 0
for i in xrange(k):
    a = start[j]
    b = end[j]
    c = off[j]
    if i == b-1:
        j += 1
    
    if height == 0:
        if c > height:
            if k - i <= height:
                ans *= 1
            
            elif k - i == height + 1:
                ans *= 2

            else:
                ans *= 2
                height += 1
        
    else:
        if c > height:
            if k - i <= height:
                ans *= 1
                height -= 1

            elif k - i == height + 1:
                ans *= 2
            
            else:
                ans *= 3
                height += 1
        
print ans