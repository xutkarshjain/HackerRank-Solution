#include<stdio.h>
//#include<conio.h>
int main()
{
    int a[3],b[3],ta=0,tb=0,i;
    scanf("%d %d %d",&a[0],&a[1],&a[2]);
    scanf("%d %d %d",&b[0],&b[1],&b[2]);
    for(i=0;i<3;i++)
    {
       //printf("%d %d \n",a[i],b[i]);
        if(a[i]>b[i])
        {
            ta++;
        }
        else if(a[i]<b[i])
        {
            tb++;
        }
    }
    printf("%d %d",ta,tb);
    return 0;
}
