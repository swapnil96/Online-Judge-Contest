'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

x = map(str, (' '.join(n for n in raw_input())).split())
y = map(str, (' '.join(n for n in raw_input())).split())

length = len(x)
ans = []
flag = 0
for i in xrange(length):

    if y[i] <= x[i]:
        ans.append(y[i])
    
    else:
        flag = 1
        break

if flag == 0:
    print ''.join(ans)

else:
    print -1