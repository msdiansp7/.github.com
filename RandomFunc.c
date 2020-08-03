#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
    /*char a,b;
    printf("1\n");
    scanf("%c",&a);
    getchar();
    printf("2\n");
    scanf("%c",&b);
    getchar();*/
    srand(time(NULL));//takes seed as a input
    printf("The random number b/w 0 and 100 is %d\n",rand()%100);
}