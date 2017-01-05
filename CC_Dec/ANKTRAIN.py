'''Link - https://www.codechef.com/DEC16/problems/ANKTRAIN'''

tt = int(raw_input())

for i in xrange(tt):

    number = int(raw_input())
    comp = number % 8
    if comp == 0:
        print str(number - 1) + "SL"

    elif comp == 7:
        print str(number + 1) + "SU"

    elif comp == 1:
        print str(number + 3) + "LB"

    elif comp == 2:
        print str(number + 3) + "MB"

    elif comp == 3:
        print str(number + 3) + "UB"

    elif comp == 4:
        print str(number - 3) + "LB"

    elif comp == 5:
        print str(number - 3) + "MB"

    elif comp == 6:
        print str(number - 3) + "UB"
