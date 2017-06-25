tt = int(raw_input())
for i in xrange(tt):
    a, b, n = map(int, raw_input().split())
    if n % 2 == 0:
        print max(a, b) / min(a, b)

    else:
        print max(2*a, b)/ min(2*a, b)
        