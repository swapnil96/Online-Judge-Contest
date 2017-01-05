length = 10**7 + 1
done = [False]*length;
smallest_prime = [0]*length

def Sieve():

    smallest_prime[0] = 0
    smallest_prime[1] = 1
    for i in xrange(2, length, 2):
        smallest_prime[i] = 2

    for i in xrange(3, length, 2):

        if done[i] == False:
            smallest_prime[i] = i
            for j in xrange(i, length/i, 2):
                if done[j*i] == False:
                    done[j*i] = True
                    smallest_prime[j*i] = i

def factorize(p):
    factors=[]
    if smallest_prime[p] == p:
        factors.append(p)
        return factors

    last = 0
    while p != 1:
        if last != smallest_prime[p]:
            factors.append(smallest_prime[p])

        last = smallest_prime[p]
        p /= smallest_prime[p]

    return factors

Sieve()
tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    a = map(int, raw_input().split())
    if n == 1:
        print 1
        continue

    dp = [0]*(10**7)
    for j in xrange(n):
        s = factorize(a[j])
        # print s
        temp = 0
        for k in s:
            temp = max(temp, dp[k-1])

        for k in s:
            dp[k-1] = temp + 1

    print max(dp)
