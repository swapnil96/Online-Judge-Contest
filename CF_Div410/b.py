'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

tt = int(raw_input())
a = []
for i in xrange(tt):
    a.append(map(str, (' '.join(n for n in raw_input())).split()))

temp = []
length = len(a[0])

for i in xrange(length):
    now = a[0][i:] + a[0][:i]
    temp.append(now)

# print temp
idx = []
for i in xrange(tt):

    flag = 1
    for j in xrange(length):
        if a[i] == temp[j]:
            flag = 0
            idx.append(j)
            break
    
    if flag == 1:
        ans = -1
        break

# print idx    
if flag == 0:
    ans = 10**9
    for i in xrange(tt):
        now = 0
        for j in xrange(tt):

            if idx[j] > idx[i]:
                now += (length + idx[i] - idx[j])

            else:
                now += idx[i] - idx[j]

        # print now
        ans = min(ans, now)

    print ans

else:
    print ans
# for i in xrange(tt):

#     for k in xrange(i + 1, tt):
        
#         for j in xrange(length):
            
#             while True:
                
#                 if a[i][j] = a[j][idx]:
                
#                 idx = (idx + 1 ) % length