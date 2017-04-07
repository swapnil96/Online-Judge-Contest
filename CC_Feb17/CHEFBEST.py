'''Link - https://www.codechef.com/FEB17/problems/CHEFBEST'''

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    a = map(int, raw_input().split())
    till_zeros = 0
    till_ones = 0
    total = 0
    dp = 0
    for j in xrange(n-1, -1, -1):
        if a[j] == 0:
            temp = till_ones - dp
            total += temp
            dp = temp
            till_zeros += 1

        else:
        	till_ones += 1


    print total
