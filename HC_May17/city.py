n, k = map(int, raw_input().split())
data = [-1]*n
for i in xrange(k):
    a = map(int, raw_input().split())
    for j in xrange(a[0]):
        data[a[1+j]-1] = i

q = int(raw_input())
query = []
for i in xrange(q):
    query.append(map(int, raw_input().split()))

for i in xrange(q):
    fm = query[i][0]
    to = query[i][1]

    if data[fm-1] == data[to-1]:
        ans = 0
    
    else:
        if data[fm-1] == 0 and data[to-1] == k-1:
            ans = 1

        elif data[fm-1] == k-1 and data[to-1] == 0:
            ans = 1

        else:
            ans = min(abs(data[fm-1]-data[to-1]), k-abs(data[fm-1]-data[to-1]))

    print ans

# print data