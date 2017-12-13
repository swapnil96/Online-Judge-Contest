from fractions import gcd

a = 10**9 + 7
b = 10**9 + 9

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

def inv(a, m):
    return pow(a, m-2, m)

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    if n == 1:
        ans = [0, 0]
    
    else:
        up = (n-1)*n
        down = 2*(2*n - 3)
        # g = gcd(up, down)
        # up /= g
        # down /= g
        # ans = [(up*modinv(down, a))%a, (up*modinv(down, b))%b]
        ans = [(up*inv(down, a))%a, (up*inv(down, b))%b]

    print ' '.join((map(str, ans)))
    
