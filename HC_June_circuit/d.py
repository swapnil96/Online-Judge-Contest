
MOD = 10**9 + 7
import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

t = int(raw_input())
a = map(int, raw_input().split())
n = t - 1
num = ((((n*(n+1)) / 2)**2) - (((n)*(n+1)*(2*n+1)*(2*n+3))/6) + (((n)*(n+1)*(n**2 + 3*n + 2))/2)) / 2
den = (t*(t-1))/2 + t
fin = pow(den, MOD - 2, MOD)
#print (num * fin ) % MOD                                                            

def SortCount(A):
   l = len(A)
   if l > 1:
      n = l//2
      C = A[:n]
      D = A[n:]
      c = SortCount(A[:n])
      d = SortCount(A[n:])
      b = MergeCount(C,D)
      return b+c+d
   else:
      return 0

def MergeCount(A,B):
   count = 0
   M = []
   while A and B:
      if A[0] <= B[0]: 
         M.append(A.pop(0)) 
      else: 
         count += len(A)
         M.append(B.pop(0)) 
   M  += A + B     
   return count 

dic = {}
ans = 0
for i in xrange(t):
	for j in xrange(i, t):
		temp = a[i:j+1]
		temp.reverse()
		temp = a[0:i] + temp + a[j+1:]
		no = SortCount(temp)
		ans += no		
		#print no, temp
		#if no not in dic:
		#	dic[no] = 1

		#else:
		#	dic[no] += 1

#ans = 0
#for j, k in dic.items():
#	ans += j*k

print (fin * ans) % MOD