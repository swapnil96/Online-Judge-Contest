'''Link - https://www.codechef.com/problems/CHEFARC'''

from Queue import Queue

def bfs(n, m, x, y, k, mat):

    inf = float("inf")
    dist = [[inf for _ in xrange(m)] for __ in xrange(n)]
    dist[x][y] = 0
    que = Queue()
    que.put((x, y, 0))
    while (not(que.empty())):
        (x1, y1, a1) = que.get()

        for x_cor in xrange(max(x1 - k, 0), min(x1 + k + 1, n)):
            d = abs(x_cor - x1)
            for y_cor in xrange(max(y1 - k + d, 0), min(y1 + k + 1 - d, m)):
                if (mat[x_cor][y_cor] == 0):
                    if (dist[x_cor][y_cor] == inf):
                        dist[x_cor][y_cor] = a1 + 1
                        que.put((x_cor, y_cor, a1 + 1))

    return dist


tt = int(raw_input())
for i in xrange(tt):
    n, m, k1, k2 = map(int, raw_input().split())
    # mat = [[0 for _ in xrange(m)] for __ in xrange(n)]
    mat = []
    for j in xrange(n):
        mat.append(map(int, raw_input().split()))

    bot1 = bfs(n, m, 0, 0, k1, mat)
    bot2 = bfs(n, m, 0, m - 1, k2, mat)
    glo = float("inf")
    for x in xrange(n):
        for y in xrange(m):
            dur = max(bot1[x][y], bot2[x][y])
            glo = min(glo, dur)

    if (glo < float("inf")):
        print glo

    else:
        print "-1"
