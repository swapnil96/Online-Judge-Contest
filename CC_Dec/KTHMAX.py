'''Link - https://www.codechef.com/problems/KTHMAX'''

import bisect

def right(arr, n):

    st = [0]*n
    a = [0]*n
    index = 0
    for i in xrange(1, n):
        while (index >= 0 and arr[i] > arr[st[index]]):
            index -= 1

        a[i] = i if index < 0 else (i - st[index] - 1)
        index += 1
        st[index] = i

    return a

def left(arr1, n):

    arr = [0]*n
    for i in xrange(n):
        arr[i] = arr1[n - i - 1]

    st = [0]*n
    a = [1]*n
    index = 0
    for i in xrange(1, n):
        while (index >= 0 and arr[i] >= arr[st[index]]):
            index -= 1

        a[i] = i + 1 if index < 0 else (i - st[index])
        index += 1
        st[index] = i

    a.reverse()
    return a

tt = int(raw_input())
for i in xrange(tt):
    n, m = map(int, raw_input().split())
    num = map(int, raw_input().split())
    query = []
    for j in xrange(m):
        query.append(int(raw_input()))

    rig = right(num, n)
    lef = left(num, n)
    temp = [0]*n
    for j in xrange(n):
        temp[j] = lef[j]*rig[j] + lef[j]

    ab = zip(num, temp)
    ab.sort(reverse = True)
    num, temp = zip(*ab)
    accumulate = [0]*n
    accumulate[0] = temp[0]
    for j in xrange(1, n):
        accumulate[j] = accumulate[j-1] + temp[j]

    for j in xrange(m):
        print num[bisect.bisect_left(accumulate, query[j])]
