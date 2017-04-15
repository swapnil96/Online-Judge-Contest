'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''
import math
n, k = map(int, raw_input().split())
fir = 2
got = 0
ans = []
if k == 1:
    ans.append(n)


while (fir <= n and k != 1):
    flag = 0
    while(True):
        if (n % fir == 0):
            ans.append(fir)
            n /= fir 
            got += 1       
            if got == k-1:
                if (n == 1):
                    flag = 1
                    break

                ans.append(n)
                got += 1
                flag = 1
                break

        if (n % fir != 0):
            fir += 1
            break

    if (flag == 1):
        break

if len(ans) == k:
    print ' '.join(map(str, ans))

else:
    print -1