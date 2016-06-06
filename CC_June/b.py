from random import randint
from fractions import gcd

def findWitness(n, k=5): # miller-rabin
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2
    for i in range(k):
        a = randint(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return a
            if x == n-1: break
        else: return a
    return 0

# returns p,k such that n=p**k, or 0,0
# assumes n is an integer greater than 1
def primePower(n):
    def checkP(n, p):
        k = 0
        while n > 1 and n % p == 0:
            n, k = n / p, k + 1
        if n == 1: return p, k
        else: return 0, 0
    if n % 2 == 0: return checkP(n, 2)
    q = n
    while True:
        a = findWitness(q)
        if a == 0: return checkP(n, q)
        d = gcd(pow(a,q,n)-a, q)
        if d == 1 or d == q: return 0, 0
        q = d

#print primePower(18)        

tt = int(raw_input())
sol = []
for i in xrange(tt):
    a = int(raw_input())
    if a % 6 == 0:
        sol.append("Misha")

    else:
        sol.append("Chef")

for i in xrange(tt):
    print sol[i]

    