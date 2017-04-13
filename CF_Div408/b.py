'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''
n, m, k = map(int, raw_input().split())
a = map(int, raw_input().split())
inp = []
got = 0
temp = [0]*n
for i in xrange(m):
    temp[a[i]-1] = 1

for i in xrange(k):
    inp.append(map(int, raw_input().split()))

now = 1
for i in xrange(k):
    x = inp[i][0]
    y = inp[i][1]
    if (x == 1 and got == 0):
        got = 1
        if temp[0] == 1:
            break

        now = y
        if temp[now-1] == 1:
            break
        # print "asdf", now

        continue

    if (y == 1 and got == 0):
        got = 1
        if temp[0] == 1:
            break
        
        # print "asdfasd", now
        now = x 
        if temp[now-1] == 1:
            break

        continue

    if (x == now):
        now = y

    elif (y == now):
        now = x

    if temp[now-1] == 1:
            break

    # print now, x, y      

print now