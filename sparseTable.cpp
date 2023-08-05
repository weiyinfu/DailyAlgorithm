#include<bits/stdc++.h>
using namespace std;

const int MAXN=100050,MAXF=18;
int ar[MAXN];
int dp[MAXN][MAXF];
int LOG[MAXN];

int main()
{
    int n,q,L,R,d;
    scanf("%d%d",&n,&q);

    LOG[1]=0;
    for(int i=2;i<=n;i++)
        LOG[i]=LOG[i/2]+1;

    for(int i=1;i<=n;i++)
    {
        scanf("%d",&ar[i]);
        dp[i][0]=ar[i];
    }

    for(int j=1;(1<<j)<=n;j++)
        for(int i=1;i+(1<<(j-1))<=n;i++)
            dp[i][j]=max(dp[i][j-1],dp[i+(1<<(j-1))][j-1]);

    while(q--)
    {
        scanf("%d%d",&L,&R);
        d=LOG[R-L+1];
        printf("%d\n",max(dp[L][d],dp[R-(1<<d)+1][d]));
    }

    return 0;
}