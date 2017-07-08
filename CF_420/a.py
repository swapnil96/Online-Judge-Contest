n = int(raw_input())
grid = []
for i in xrange(n):
    grid.append(map(int, raw_input().split()))

flag = 1
for i in xrange(n):
    for j in xrange(n):
        ele = grid[i][j]
        if ele == 1:
            continue

        flag = 0
        for k in xrange(n):
            if k == i:
                pass

            for l in xrange(n):
                if l == j:
                    pass
                
                if grid[i][l] + grid[k][j] == ele:
                    flag = 1

        # print flag, ele    
        if flag == 0:
            break
    
    if flag == 0:
        break

if flag == 0:
    print "No"

else:
    print "Yes"
