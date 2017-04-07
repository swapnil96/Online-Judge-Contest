'''Link - https://www.codechef.com/JAN17/problems/CAPIMOVE'''

tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    # road = [[0 for __ in xrange(n)] for _ in xrange(n)]
    a = map(int, raw_input().split())
    name = [j for j in xrange(n)]
    road = {}
    for j in xrange(n):
        road[j] = []
        road[j].append(j)

    for j in xrange(n - 1):
        u, v = map(int, raw_input().split())
        road[u-1].append(v-1)
        road[v-1].append(u-1)
        # road[u-1][v-1] = 1
        # road[v-1][u-1] = 1
        # road[j][j] = 1

    # road[n-1][n-1] = 1
    ab = zip(a, name)
    ab.sort(reverse = True)
    a, name = zip(*ab)
    # name = [y for (x,y) in sorted(zip(a, name))]
    # a.sort()
    # print a, name, road
    ans = []
    for j in xrange(n):
        ans.append(0)
        for k in xrange(n):
            # if road[j][name[k]] == 0:
            #     ans[j] = name[k] + 1
            #     break
            if j not in road[name[k]]:
                ans[j] = name[k] + 1
                break

    print ' '.join(map(str, ans))
