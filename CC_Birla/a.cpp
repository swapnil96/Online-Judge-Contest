#include <bits/stdc++.h>
using namespace std;

void solve()
{
	int m;
    scanf("%d", &m);
    priority_queue<long long, vector<long long>, greater<long long> >pq;
    long long int x, ans;
    for(int i = 0; i < m; i++)
    {
		scanf("%lld", &x);
		pq.push(x);
	}
    ans = 0;
    long long int u, v;
    while(!pq.empty())
    {
        u = pq.top();
		pq.pop();
		if (pq.empty()) 
				break;

		v = pq.top();
		pq.pop();
		ans += u + v - 1;
		pq.push(u + v);
    }
    printf("%lld\n", ans);
}


int main(int argc, char const *argv[])
{
    int tt;
    scanf("%d", &tt);
    while(tt--)
        solve();
    
    return 0;
}
