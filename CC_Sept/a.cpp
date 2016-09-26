#include <bits/stdc++.h>
using namespace std;
 
long long inf = 100000000000001ll;        // 10^5 * 10^9 = 10^14
 
//fastio to decrease execution time
long scan_long() {
    long num = 0;
    register char c = getchar_unlocked();
    while (c < '0' || c > '9') {
        c = getchar_unlocked();
    }
    for(; c >= '0' && c <= '9'; c = getchar_unlocked()) {
        num = (num << 3) + (num << 1) + (c & 15);
    }
    return num;
}
 
void prlong_long_long(long long n) {
    char snum[65]; 
    long i = 0; 
    do {
        snum[i++] = n % 10 + '0';
        n /= 10;
    } while(n);
    i = i - 1;
    while (i >= 0) {
        putchar_unlocked(snum[i--]);
    }
    putchar_unlocked('\n');  
}
 
struct node {
    long len;
    long cost;
};
 
vector< long > transpose[100001];
vector< node > vertex[100001]; 
long long minimise[100001];
long depth[100001];
long lca[18][100001];
long long small[18][100001];
 
void fastio() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}
 
//directed graph so no need of malongaining visited array
void compute(long start) {
    for(vector< long >::iterator it = transpose[start].begin(); it != transpose[start].end(); ++it) {
        //first update the values and then query
        long to = *it;
        small[0][*it] = minimise[lca[0][to]];
        to = lca[0][*it];
        long height = 31 - __builtin_clz(depth[*it]);
        //cout<<height<< "asddf" << small << endl;
        for(long ctr = 1; ctr <= height; ++ctr) {
            if (to == -1) {
                break;
            }
            small[ctr][*it] = min(small[ctr-1][*it], small[ctr-1][to]);
            to = lca[ctr][*it];
        }
        for(vector< node >::iterator it2 = vertex[*it].begin(); it2 != vertex[*it].end(); ++it2) {
            if (it2->len >= depth[*it]) {       //base case i.e. reach directly
                minimise[*it] = min(minimise[*it], (long long)it2->cost);
            }
            else {
                to = *it;
                long long val = inf;
                for(long ctr = 0; ctr <= height; ++ctr) {
                    if (to == -1) {
                        break;
                    }
                    if (it2->len & (1 << ctr)) {
                        //cout << "got"<<it2->len<<endl;
                        val = min(val, small[ctr][to]);
                        to = lca[ctr][to];
                    }
                }
                minimise[*it] = min(minimise[*it], it2->cost + val);
            }
        }
        compute(*it);
    }
}
 
//directed graph so no need of malongaining visited array
void dfs(long start, long p, long d) {
    lca[0][start] = p;
    depth[start] = d;
    for(vector< long >::iterator it = transpose[start].begin(); it != transpose[start].end(); ++it) {
        dfs(*it, start, d + 1);
    }
}
 
int main() {
    // fastio();
    long n, m, q, x, a, b;
    n = scan_long();
    m = scan_long();
    for(long i = 0; i < n - 1 ; ++i) {
        a = scan_long();
        b = scan_long();
        transpose[b].push_back(a);
    }
    memset(lca, -1, sizeof lca);
    dfs(1, -1, 0);
    //build lca table
    for(long i = 1; i < 19; ++i) {
        for(long j = 1; j <= n; ++j) {
            if (lca[i-1][j] != -1) {
                lca[i][j] = lca[i-1][lca[i-1][j]];
            }
        }
    }
    for(long i = 0; i < m; ++i) {
        x = scan_long();
        a = scan_long();
        b = scan_long();
        node temp;
        temp.len = a;
        temp.cost = b;
        vertex[x].push_back(temp);
    }
    memset(minimise, inf, sizeof minimise);
    memset(small, inf, sizeof small);
    minimise[1] = 0;        //base case
    compute(1);
    q = scan_long();
    for(long i = 0; i < q; ++i) {
        x = scan_long();
        //cout << minimise[x];
        prlong_long_long(minimise[x]);
    }
    return 0;
} 