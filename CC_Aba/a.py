'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

tt = int(raw_input())
for i in xrange(tt):
    m, n = map(int, raw_input().split())
    if (m % 2 == 0):
        print "VADA"

    else:
        print "IDLY"
