#include<stdio.h>
int main()
{
        int n,i,j,dl=0,dr=0;
        scanf("%d",&n);
        int a[n][n];
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        
        for(i=0;i<n;i++)
        {
            dl=dl+a[i][i];
            dr=dr+a[i][n-i-1];
        }
        if(dr>dl)
            printf("%d",dr-dl);
        else
            printf("%d",dl-dr);
    return 0;

}
