'''Link - https://www.codechef.com/JAN17/problems/TOURISTS'''

class Node:

    def __init__(self, data, pre = None, nex = None):
        self.data = data
        self.pre = pre
        self.nex = nex

class List:

    def __init__(self):
        self.head = Node(-1, None, None)
        self.tail = self.head
        self.size = 0

    def add(self, nod):
        self.size += 1
        self.tail.nex = nod
        nod.pre = self.tail
        nod.nex = None
        self.tail = nod

    def remove(self, data = None):
        self.size -= 1
        if data == None:
            temp = self.head.nex
            self.head.nex = temp.nex
            self.head.nex.pre = self.head
            del temp

        else:
            temp = self.head
            while temp.data != data:
                temp = temp.nex

            temp.pre.nex = temp.nex
            if temp.nex != None:
                temp.nex.pre = temp.pre
                del temp

    def delete(self):

        self.size -= 1
        temp = self.tail.data
        temp1 = self.tail
        self.tail = self.tail.pre
        self.tail.nex = None
        del temp1
        return temp

    def last(self):

        return self.tail.data

    def front(self):

        return self.head.nex.data

    def contains(self, data):

        temp = self.head
        while temp != None:
            if temp.data == data:
                return temp

            temp = temp.nex

        return None

    def pr(self):

        temp = self.head.nex
        while temp != None:
            print temp.data
            temp = temp.nex

def dfs(dic, start, n):

    temp = List()
    final = []
    temp.add(Node(start))
    s = start
    checking = [0]*n
    while temp.size != 0:
        vertex = temp.last()
        if (dic[vertex].size != 0):
            to = dic[vertex].front()
            temp.add(Node(to))
            dic[vertex].remove(to)
            dic[to].remove(vertex)

        if temp.last() == s:
            while True:
                if temp.size == 0:
                    break

                if dic[temp.last()].size == 0:
                    d = temp.delete()
                    checking[d] = 1
                    final.append(d)

                else:
                    s = temp.last()
                    break

    if sum(checking) == n:
        return [True, final]

    return [False, final]

n, e = map(int, raw_input().split())
road = {}
det = {}
repet = [0]*n
n_done = [1]*n
for i in xrange(n):
    road[i] = List()
    det[i] = {}

form = []
for i in xrange(e):
    u, v = map(int, raw_input().split())
    form.append([u, v])
    repet[u-1] += 1
    repet[v-1] += 1
    road[u - 1].add(Node(v - 1))
    road[v - 1].add(Node(u - 1))

got = 0
for i in xrange(n):
    if repet[i] % 2 != 0 or repet[i] == 0:
        got = 1
        break

if got == 1:
    print "NO"

else:
    flag, route = dfs(road, 0, n)
    if flag == False:
        print "NO"

    else:
        print "YES"
        for i in xrange(e):
            det[route[i]][route[i+1]] = 1

        for i in xrange(e):
            u, v = form[i]
            try:
                if det[u-1][v-1] == 1:
                    print u, v

            except:
                print v, u
