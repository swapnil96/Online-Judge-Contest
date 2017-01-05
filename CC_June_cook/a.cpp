#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <bitset>
#include <string>
#include <cstring>
#include <queue>
#include <cassert>
#define rf freopen("in.in", "r", stdin)
#define wf freopen("out.out", "w", stdout)
#define rep(i, s, n) for(int i=int(s); i<=int(n); ++i)
using namespace std;
const int mx = 1e5 + 10, mod = 1e9+7;

char input[2000][2000];
static int cumXor[2000][2000];
bitset<2000> bits[2000];
int n, m;

long long ans = 0;

int main() {
	//rf;// wf;
	ios::sync_with_stdio(0);

	cin >> n >> m;
	rep(i, 0, n-1){
		cin >> input[i];
	}

	rep(i, 1, n) rep(j, 1, m) {
		cumXor[i][j] = input[i-1][j-1] - '0';
		cumXor[i][j] ^= cumXor[i-1][j];
		cumXor[i][j] ^= cumXor[i][j-1];
		cumXor[i][j] ^= cumXor[i-1][j-1];

		bits[i][j] = cumXor[i][j];
	}

	rep(i, 1, n) rep(j, 0, i-1) {
		int x = (bits[i]^bits[j]).count();
		int y = m+1 - x;

		ans += (1ll*x*(x-1))/2;
		ans += (1ll*y*(y-1))/2;
	}
	cout << ans << endl;

	return 0;
}
