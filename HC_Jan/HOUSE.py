'''Link - https://www.hackerearth.com/january-circuits-17/algorithm/micros-house-30/'''

class Node:

    def __init__(self, digit = None):
        self.digit = digit
        self.right = None
        self.left = None

    def insert_help(self, s, idx = 0):

        if idx > 26:
            return

        ch = s[idx]
        idx += 1
        if ch == '0':
            if self.left == None:
                self.left = Node(s[:idx])

            self.left.insert_help(s, idx)

        else:
            if self.right == None:
                self.right = Node(s[:idx])

            self.right.insert_help(s, idx)

    def search(self, s, till = "", idx = 0):

        if idx > 26:
            return till

        ch = s[idx]
        idx += 1
        # print ch, 'checkgin'
        if ch == '0':
            if self.right == None:
                # print 'checek 1'
                if self.left == None:
                    return till

                else:
                    till += "0"
                    # print 'chech ', idx, " ", till
                    till = self.left.search(s, till, idx)

            else:
                till += "1"
                till = self.right.search(s, till, idx)

        else:
            if self.left == None:
                if self.right == None:
                    return till

                else:
                    till += "0"
                    till = self.right.search(s, till, idx)

            else:
                till += "1"
                till = self.left.search(s, till, idx)

        return till

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, num):
        a = bin(num)[2:]
        l = len(a)
        s = ""
        for i in xrange(27-l):
            s += "0"

        s += a
        self.root.insert_help(s)

    def query(self, num):
        a = bin(num)[2:]
        l = len(a)
        s = ""
        for i in xrange(27-l):
            s += "0"

        s += a
        return self.root.search(s)

def max_seq(l):

    t = Trie()
    ans = 0
    pre = 0
    t.insert(0)
    for i in xrange(n):
        pre = pre ^ l[i]
        # print pre, 'pre'
        t.insert(pre)
        # print int(t.query(pre), 2)
        ans = max(ans, int(t.query(pre), 2))

    return ans

n, m = map(int, raw_input().split())
mat = [[] for _ in xrange(m)]
for i in xrange(n):
    x = map(int, raw_input().split())
    for j in xrange(m):
        mat[j].append(x[j])


# print mat
l = 0
r = 0
cur_xor = 0
max_xor = 0
max_left = 0
max_right = 0
max_up = 0
max_down = 0
temp = [0]*n
fin = 0
for i in xrange(m):

    temp = mat[i]
    cur_xor = max_seq(temp)
    # print cur_xor, 'in i'
    max_xor = max(max_xor, cur_xor)
    for j in xrange(i+1, m):

        for k in xrange(n):
            temp[k] ^= mat[j][k]

        # print temp
        cur_xor = max_seq(temp)
        # print cur_xor, "in j"
        max_xor = max(max_xor, cur_xor)

print max_xor
