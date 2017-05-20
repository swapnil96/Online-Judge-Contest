#include <iostream>
#include<bits/stdc++.h>
using namespace std;
double  lim, currsum;
long long int ans=0;
int n,considered;
void fun(double arr[],double CurrentSum,double MaxSum,int index, int considered)
{
    
    if(CurrentSum>MaxSum)
       return;
    else if(CurrentSum<=MaxSum && index!=-1 && considered==1)
       ans++;
    
   // cout<<"Current sum is "<<CurrentSum<<endl;
    //cout<<"Element being considered is "<<arr[index+1]<<" index is "<<index<<endl;
    //cout<<"Ans is "<<ans<<endl;
    //cout<<"Max Sum is "<<MaxSum<<endl;
    if(index+1>=n)
      return;
    fun(arr,CurrentSum+arr[index+1],lim,index+1,1);
    fun(arr,CurrentSum,lim,index+1,0);
}
 
int main() {
	// your code goes here
 
	long long int k;
	cin>>n>>k;
	double arr[n],sum;
	int i,j;
	for(i=0;i<n;i++)
	{
	    cin>>arr[i];
	    arr[i]=log(arr[i]);
	   // sum+=arr[i];
	}
	sort(arr,arr+n);
	lim=log(k);
	int el=n;
	for(i=0;i<n;i++)
	{
	    if (arr[i]>lim)
	       el--;
	}
	sum=0;
	for(i=0;i<n;i++)
	   sum+=arr[i];
	n=el;
	int start=0;
	for(i=0;i<n;i++)
	{
	    if(arr[i]==0)
	       {
	           start++;
	           //ans+=pow(2,n-i-1);
	       }
	}
	
	if(sum<=lim)
	  ans=pow(2,n)-1;
	else  
	  fun(arr,0,lim,start-1,0);
	//cout<<"Ans atm is "<<ans<<endl;
	while(start--)
	   ans= ans+(ans+1);
	cout<<ans<<endl;
	
	return 0;
}