# dp solution
# import math

# n, k = map(int, raw_input().split())
# a = map(int, raw_input().split())

# # k = math.log10(kk)

# dp = [[0 for _ in xrange(sum(a))] for __ in xrange(n)]
# print dp

# for i in xrange(n):

#     dp[i][a[i]] = 1
#     print dp
#     if i == 0:
#         continue

#     for j in xrange(1, k):
#         dp[i][j] += dp[i-1][j]
    
#     for j in xrange(k):
#         if j + a[i] >= k:
#             break
        
#         dp[i][j+a[i]] += dp[i-1][j]
    
# ans = 0
# for i in xrange(1, k):
#     ans += dp[n-1][i]
    
# print ans
# print dp

import math
import bisect

import sys

# n, kk = map(int, raw_input().split())
# aa = map(int, raw_input().split())

n, kk = map(int, sys.stdin.readline().split())
aa = map(int, sys.stdin.readline().split())

a = map(math.log10, aa)
k = math.log10(kk)
star = 0
for i in a:
    if i != 0:
        break
    
    star += 1

end = n
for i in xrange(n-1, -1, -1):
    if a[i] <= k:
        break
    
    end -= 1

tot = sum(a)
a.sort()
ans = 0
# def recur(arr, start, end, size, s):

#     pos = bisect.bisect(arr, s, start, end) - 1

#     global ans    
#     if pos > 0:
#         recur(arr, start, pos, size-1, s-arr[pos])
#         recur(arr, start, pos, size-1, s)

#     elif pos == 0:
#         ans += 2

#     else:
#         ans += 1

def recur(arr, index, curr_sum, req_sum, taken):

    if curr_sum > req_sum:
        return 
    
    global ans    
    global n

    if curr_sum <= req_sum and index != -1 and taken == 1:
        ans += 1
    
    if index + 1 >= n:
        return 
    
    recur(arr, index + 1, curr_sum + arr[index+1], req_sum, 1)
    recur(arr, index + 1, curr_sum, req_sum, 0)

if tot <= k:
    ans = 2**n - 1

else:
    n = end
    recur(a, star-1, 0, k, 0)
    while star != 0:
        ans += ans + 1
        star -= 1

print ans 

