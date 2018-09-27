#include <stdio.h>
int main()
{
	int number;
	printf("请输入一个数：");
	scanf("%d",&number);

	if(number%2==0){
	if(number%3==0) printf("这个数可以被2和3整除\n");
	else printf("这个数只能被二整除，但不可以被3整除\n");
}
	else if(number%3==0) printf("这个数不可以被2整除，但能被3整除\n");
	else printf("这个数既不能被2整除，也不能被3整除\n");

	return 0;
}
