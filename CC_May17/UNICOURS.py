tt = int(raw_input())

for i in xrange(tt):
    n = int(raw_input())
    a = map(int, raw_input().split())

    print n - max(a)
    