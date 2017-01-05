'''Link - https://www.codechef.com/DEC16/problems/KIRLAB'''

def primes(n):
    primfac = set()
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.add(d)
            n //= d

        d += 1

    if n > 1:
       primfac.add(n)

    return primfac

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    a = map(int, raw_input().split())
    b = [1]*n
    gcount = 1
    ncount = 0
    primesfac = []
    for j in xrange(n):
        primesfac.append(primes(a[j]))

    for j in xrange(1, n):
        for k in xrange(j-1, -1, -1):
            if (len(primesfac[j].intersection(primesfac[k]))):
                if b[k] >= b[j]:
                    b[j] = b[k] + 1
                    if b[j] > gcount:
                        gcount = b[j]

    print gcount

def sieve():
    for i in range(2,MAX,2): sp[i]=2

    for i in range(3,MAX,2):
        if not v[i]:
            sp[i]=i
            j=i
            while j*i<MAX:
                if not v[j*i]:
                    v[j*i]=True
                    sp[j*i]=i
                j+=2

MAX=10**7+1
from math import sqrt
from collections import defaultdict
v=defaultdict(lambda:False)
sp=defaultdict(int)
sieve()
for _ in range(int(raw_input())):
    count=defaultdict(int)
    n=int(raw_input())
    arr=map(int,raw_input().split())
    if n==1:
        print 1
    else:
        for i in range(n):

            factors=[]
            p=arr[i]
            last=0
            while p!=1:
                if last!=p:
                    factors.append(sp[p])
                last=sp[p]
                p=p/sp[p]

            update=0
            for each in factors:
                update=max(update,count[each])
            for each in factors:
                count[each]=update+1
        try:
            print max(count.values())
        except:
            print 1
