#include<stdio.h>
#include<string.h>

//Global variable

int a=6;

int func1()
{
	//static variable
	
	static int c=5;
	printf("%d\n",c);
	c++;
}

int main()
{
    //local variable
    
    int a=7;
    func1();
    func1();
    printf("%d\n",a);
}