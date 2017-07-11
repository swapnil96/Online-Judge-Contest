tt = int(raw_input())
for i in xrange(tt):
    a = raw_input()
    gre = 1
    low = 1
    curr_gre = 1
    curr_low = 1
    for j in xrange(len(a)):
        if a[j] == '<':
            curr_low = 1
            curr_gre += 1

        elif a[j] == '=':
            pass
        
        else:
            curr_gre = 1
            curr_low += 1

        gre = max(gre, curr_gre)
        low = max(low, curr_low)

    print max(low, gre)