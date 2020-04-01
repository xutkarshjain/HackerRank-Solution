#include<stdio.h>
int main()
{
    int n,i;
    float plus=0,minus=0,zero=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
      {
        if(a[i]==0)
            zero++;
        else if(a[i]>0)
            plus++;
        else if(a[i]<0)
            minus++;
       }
    printf("%f\n%f\n%f",plus/n,minus/n,zero/n);
return 0;
}
