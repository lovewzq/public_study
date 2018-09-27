#include <Stdio.h>
int main()
{
    int m,n,i,a[4];

    printf("请输入范围（m~n)：\n");
    scanf("%d %d",&m,&n);


    for(i=m;i<=n;i++){
     a[0]=i%10;      //个位
     a[1]=i/10%10;   //十位
     a[2]=i/100;     //百位
     a[3]=a[0]*a[0]*a[0]+a[1]*a[1]*a[1]+a[2]*a[2]*a[2];
     if(a[3]==i){
        printf("%d",a[3]);
        printf("\n");
     }
    }
    return 0;
    }
