tt = int(raw_input())
for i in xrange(tt):
    a = map(str, raw_input().split())
    if len(a) == 1:
        temp = a[0][0].upper()
        temp += a[0][1:].lower()
        print temp
    
    elif len(a) == 2:
        temp = a[0][0].upper()
        temp += ". "
        temp += a[1][0].upper()
        temp += a[1][1:].lower()
        print temp
    
    else:
        temp = a[0][0].upper()
        temp += ". "
        temp += a[1][0].upper()
        temp += ". "
        temp += a[2][0].upper()
        temp += a[2][1:].lower()
        print temp
    
