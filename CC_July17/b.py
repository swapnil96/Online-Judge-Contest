

class node:
    def __init__(self, count, left, right):
        self.count = count
        self.left = left
        self.right = right

    def insert(self, l, r, w):
        if l <= w and w < r:
            if l + 1 == r:
                return node(self.count+1, null, null)
            
            m = (l + r)>>1
            return node(self.count + 1, self.left.insert(l, m, w), self.right.insert(m, r, w))

        return self

def dfs(curr, prev):

    pa[cur][0] = prev
    depth[cur] = 0 if prev == -1 else depth[prev] + 1
    root[cur] = (null if prev == -1 else root[prev]).insert(0, maxi, M[v[curr]])
