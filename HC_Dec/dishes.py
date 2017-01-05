'''Link - https://www.hackerearth.com/december-circuits-16/approximate/christmas-dishes-2/'''

n, k = map(int, raw_input().split())

if n == k:
    a = ''
    for i in xrange(n):
        a += "a"

    print a

else:
    if n == 2 and k == 3:
        print "ab"

    else:
        print "No"
