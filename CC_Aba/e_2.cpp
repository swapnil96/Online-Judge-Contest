#include <bits/stdc++.h>

using namespace std;
typedef long long INT;
typedef pair <int ,int> pii;
#define NN 1111111
#define MOD 1000000007

INT fac[NN];

int main (){


	int M,N;
	int i,j;
	fac[1]=1;
	for(i=2;i<NN;i++){
		fac[i]=fac[i-1]*i%MOD;
	}
	while(~scanf("%d%d",&M,&N)){
		if(M>N) swap(M,N);
		INT ans=1;
		for(i=2;i<M;i++){
			ans=fac[i]*ans%MOD;
		}
		ans=ans*ans%MOD;
		for(i=0;i<N-M+1;i++)
			ans=ans*fac[M]%MOD;
		printf("%lld\n",ans);
	}

	return 0;
}
