'''Problem name - SEBSEG2 from Codechef'''
'''explanation link - https://discuss.codechef.com/questions/81931/subseg2-editorial'''

tt = map(int, raw_input().split())
'''
def printMaxActivities(s, que):
    
    #f, s = zip(*sorted(zip(f, s)))
    s = sorted(s,key=lambda l:l[1])
    #print s
    n = tt[0]
    i = 0
    #sol1 = []
    ans = 0
    got = 0
    for j in xrange(n):
        if s[j][0] >= que[0] and s[j][1] <= que[1]:
            #print 'qwer', j, que[1], s[j][0]
            ans += 1
            i = j
            got = 1
            break

    if got == 0:
        return 0

    #sol1.append(i)
    #print sol1, que
    # Consider rest of the activities
    for j in xrange(n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously 
        # selected activity, then select it
        if s[j][1] <= que[1]:
            if s[j][0] >= que[0]:
                #print 'asdf', j
                if s[j][0] >= s[i][1]:
                #sol1.append(j)
                    ans += 1
                    i = j

        else:
            #print j
            break        

    #print sol1            
    return ans
'''
'''
start = []
#finish = []
for i in xrange(tt[0]):
    a = map(int, raw_input().split())
    start.append([a[0], a[1]])
    #finish.append(a[1])

sol = []
for i in xrange(tt[1]):
    sol.append(printMaxActivities(start, map(int, raw_input().split())))

for i in xrange(tt[1]):
    print sol[i]

'''

L = []
for i in xrange(tt[0]):
    S = raw_input().split()
    L.append([int(S[0]),int(S[1])])
    L = sorted(L,key=lambda l:l[1])

sol = []
for i in xrange(tt[1]):
    a = map(int, raw_input().split())
    count = 0
    i = 0
    #print L, a
    got = 0
    for j in xrange(tt[0]):
        if L[j][0] >= a[0] and L[j][1] <= a[1]:
            #print 'qwer', j, que[1], s[j][0]
            count += 1
            i = j
            got = 1
            break
           
    if got == 0:
        #sol.append(0)
        print 0
        continue
    
    for j in xrange(tt[0]):
        
        if L[j][1] <= a[1]:
            if L[j][0] >= a[0]:
                #print 'asdf', j
                if L[j][0] >= L[i][1]:
                #sol1.append(j)
                    count += 1
                    i = j

        else:
            #print j
            break 
    
    print count
'''
for i in xrange(tt[1]):
    print sol[i]    
'''
   