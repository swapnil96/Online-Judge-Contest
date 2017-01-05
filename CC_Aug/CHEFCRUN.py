'''Link - https://www.codechef.com/problems/CHEFCRUN'''

def kadane(a, n, l, r):

    i = l
    glo = 0
    imm = 0
    while i != r:
        imm = max(0, imm + a[i])
        glo = max(glo, imm)
        i = (i + 1) % n

    return glo

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    a = map(int, raw_input().split())
    start, end = map(int, raw_input().split())
    start -= 1
    end -= 1
    clock = 0
    anticlock = 0
    i = start
    while i != end:
        clock += a[i]
        i += 1

    i = end
    while i != start:
        anticlock += a[i]
        i = (i + 1) % n

    clk = kadane(a, n, start, end)
    aclk = kadane(a, n, end, start)

    Tclk = clock + 2*(anticlock - aclk)
    Taclk = anticlock + 2*(clock - clk)

    print min(Tclk, Taclk)
