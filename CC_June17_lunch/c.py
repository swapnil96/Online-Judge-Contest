tt = int(raw_input())
for i in xrange(tt):
    n, x = map(int, raw_input().split())
    p = map(int, raw_input().split())
    c = map(int, raw_input().split())
    k = map(int, raw_input().split())
    club = {}
    level = {}
    for j in xrange(n):
        try:
            t = club[c[j]]
            club[c[j]].append(j)
            level[c[j]].append(k[j])

        except:
            club[c[j]] = [j]
            level[c[j]] = [k[j]]

    anc = {}
    for j in xrange(n-1):
        par = p[j]
        chi = j + 1
        while True:
            try:
                t = anc[par]
                anc[par][j+1] = 1
    
            except:
                anc[par] = {j+1: 1}
    
            if par == 0:
                break

            chi = par   
            par = p[par-1]
    
    ans = [0]*n
    for j in club:
        mem = club[j]
        lev = level[j]
        s = zip(lev, mem)
        s.sort()
        lev = [q for (q, w) in s]
        mem = [w for (q, w) in s]
        for k in xrange(len(mem)):
            if lev[k] == 0:
                ans[mem[k]] = 1
                pass

            else:
                for l in xrange(k-1, -1, -1):
                    if lev[k] - 1 == lev[l]:
                        try:
                            t = anc[mem[k]][mem[l]] 
                            ans[mem[k]] += ans[mem[l]]

                        except:
                            pass
                    
                    elif lev[k] == lev[l]:
                        pass
                    
                    else:
                        break

    for j in xrange(n):
        print ans[j]