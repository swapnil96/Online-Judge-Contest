#include <bits/stdc++.h>
using namespace std;

void solve(int M, int N)
{
    long long int NN = 1111111;
    long long int MOD = 1000000007;
    // printf("%s\n","why" );
    int fac[NN];
    int i,j;
    fac[0] = 1;
	fac[1] = 1;
	for(i=2; i<NN; i++)
		fac[i] = fac[i-1]*i % MOD;

	if(M>N) swap(M,N);
	long long int ans = 1;
	for(i=2; i<M; i++){
		ans = fac[i]*ans %MOD;
	}
	ans = ans*ans % MOD;
	for(i=0; i<N-M+1; i++)
	   ans = ans*fac[M] % MOD;

    printf("%lld\n",ans);
}


int main ()
{
    int M, N;
    scanf("%d %d",&M, &N);
    solve(M, N);
	return 0;
}
