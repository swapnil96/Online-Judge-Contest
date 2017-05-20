
tt = int(raw_input())
for i in xrange(tt):
    s = raw_input()
    length = len(s)
    state = 0
    ans = "yes"
    for j in xrange(length):

        if state == 0 and s[j] == 'C':
            pass
        
        elif state == 0 and s[j] == 'E':
            state = 1

        elif state == 0 and s[j] == 'S':
            state = 2

        elif state == 1 and s[j] == 'E':
            pass

        elif state == 1 and s[j] == 'S':
            state = 2
        
        elif state == 2 and s[j] == 'S':
            pass
        
        else:
            ans = "no"
    
    print ans