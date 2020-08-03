#include<stdio.h>
#include<stdlib.h>
#define CA(x) (3.14*x*x)

int main()
{
//	int a=cbrt(8);
//	printf("%d\n",a);
//	float r=3;
//	int CArea=CA(r);
//	printf("%f\n",CArea);
//printf("This files's name is %s ",__FILE__);

//converting binary to decimal
     
     int a=010111;
     int ans=0,Dec=0;
     for(int i=0;i<12;i++)
     {
         if(a != 0)
         {
             ans = a%10;
             
             a=a/10;
             Dec=Dec+(ans*pow(2,i));
             
         }
         
     }
     printf("%d\n",Dec);
     printf("%d",sizeof(Dec));
     
}