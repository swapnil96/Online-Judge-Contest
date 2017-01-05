'''Link - https://www.codechef.com/problems/SHAIKHGN'''

import numpy

n = int(raw_input())
a = []
for i in xrange(n):
	a.append(map(int, raw_input().split()))

array = numpy.matrix(a)
pre = []
pre.append(array)
for i in xrange(30):
	temp = pre[i]**2
	pre.append(temp)

# print pre
q = int(raw_input())
for i in xrange(q):
    k, x = map(int, raw_input().split())
    b = bin(k)[2:]
    length = len(b)
    temp = numpy.identity(n)
    for j in xrange(length):
        if b[j] == '1':
            temp = temp * pre[length - j - 1]
            # print pre[j]

    ans = []
    for j in xrange(n):
        if temp[x - 1, j] > 0:
            ans.append(j + 1)

    if len(ans) == 0:
        print 0
        print -1

    else:
        print len(ans)
        print ' '.join(map(str, ans))
