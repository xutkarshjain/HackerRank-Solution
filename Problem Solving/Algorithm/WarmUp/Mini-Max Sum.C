    #include<stdio.h>
int main()
{
    long int  a[5],i,min,max,sum=0;
    for(i=0;i<5;i++)
    scanf("%ld",&a[i]);
    min=a[0];
    max=a[0];
    //for min and max
    for(i=0;i<5;i++)
    {
        sum=sum+a[i];
        if(a[i]<min)
            min=a[i];
        if(a[i]>max)
            max=a[i];
    }
    printf("%ld %ld",sum-max,sum-min);
    return 0;

}
