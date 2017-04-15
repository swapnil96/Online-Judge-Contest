
n = int(raw_input())
a = map(int, raw_input().split())
odd = []
even = []
odd_neg = []
even_neg = []
l_odd = 0
l_even = 0
even_sum = 0
odd_sum = 0
low_odd_neg = -100000
odd_low = 10000
for i in xrange(n):

    if a[i] < 0:
        t = -1*a[i]
        if (t % 2 == 0):
            even_neg.append(a[i])
    
        else:
            odd_neg.append(a[i])
            low_odd_neg = max(low_odd_neg, a[i])

    else:
        if (a[i] % 2 == 0):
            even.append(a[i])
            l_even += 1
            even_sum += a[i]
    
        else:
            odd.append(a[i])
            l_odd += 1
            odd_low = min(odd_low, a[i])
            odd_sum += a[i]

# low_even_neg = min(even_neg)
ans = 0
if (odd_sum % 2 == 0):
    if (l_odd != 0):
        ans += odd_sum + even_sum
        ans = max(ans - odd_low, ans + low_odd_neg)
    
    else:
        if (l_even == 0):
            ans = low_odd_neg            

        else:
            ans += even_sum + low_odd_neg
    
else:
    ans += odd_sum + even_sum

print ans



