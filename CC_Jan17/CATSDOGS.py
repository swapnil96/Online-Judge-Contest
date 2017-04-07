'''Link - https://www.codechef.com/JAN17/problems/CATSDOGS'''

tt = int(raw_input())
for i in xrange(tt):
    c, d, l = map(int, raw_input().split())

    if l % 4 != 0:
        print "no"

    else:
        if d * 4 > l:
            print "no"

        else:
            l -= d * 4
            if c * 4 < l:
                print "no"

            else:
                c -= l / 4
                if d * 2 < c:
                    print "no"

                else:
                    print "yes"
