'''Link - https://www.hackerearth.com/december-circuits-16/approximate/christmas-divisors/'''

k = int(raw_input())
powers = []
divisors = 1
for i in xrange(k):
    powers.append(map(int, raw_input().split()))
    divisors *= (powers[i][1] + 1)

print divisors
ans = []

for j in xrange(k):
    for l in xrange(1, powers[j][1] + 1):
        ans.append(powers[j][0]**l)

print ans
