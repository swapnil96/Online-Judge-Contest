
class Trie_node:

    def __init__(self):
        self.child = {}

    def insert_help(self):
        return 

    def search_help(self, string, temp):

        try:
            return self.child[string[0]].search_help(string[1:], temp + string[0])
        
        except:
            if string == "":
                return -1

            return (temp + string[0])
   
    def print_help(self):

        for i in self.child:
            print i
            self.child[i].print_help()

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, string):
        try:
            self.root[string[0]].insert_help()
            temp = self.root[string[0]]
            
        except:
            temp = Trie_node()
            self.root[string[0]] = temp
        
        for i in xrange(1, len(string)):
            try:
                temp.child[string[i]].insert_help()
                temp = temp.child[string[i]]

            except:
                temp1 = Trie_node()
                temp.child[string[i]] = temp1
                temp = temp1
    
    def search(self, string):

        try: 
            return self.root[string[0]].search_help(string[1:], string[0])

        except:
            return string[0]

    def print_trie(self):
        for i in self.root:
            print i
            self.root[i].print_help()


n = int(raw_input())
block = []
n_block = []

for i in xrange(n):
    a = raw_input().split()
    if a[0] == "+":
        n_block.append(a[1])
    
    else:
        block.append(a[1])

trie = Trie()
for i in xrange(len(n_block)):
    trie.insert(n_block[i])

ans = []
for i in xrange(len(block)):
    fin = trie.search(block[i])
    if fin == -1:
        print -1
        exit(0)
    
    ans.append(fin)

ans = list(set(ans))
ans.sort()
print len(ans)
for i in xrange(len(ans)):
    print ans[i]

