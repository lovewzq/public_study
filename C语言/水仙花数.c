#include <stdio.h>
  void main()
{
	int i,a,b,c;
	for(i=100;i<=999;i++)
	{
		a=i/100;  //百位
		b=i%100/10;//十位
		c=i%10;//个位

	if(a*a*a+b*b*b+c*c*c==i) printf("%d ",i);
	}
}
