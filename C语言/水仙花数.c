#include <stdio.h>
  void main()
{
	int i,a,b,c;
	for(i=100;i<=999;i++)
	{
		a=i/100;  //��λ
		b=i%100/10;//ʮλ
		c=i%10;//��λ

	if(a*a*a+b*b*b+c*c*c==i) printf("%d ",i);
	}
}
