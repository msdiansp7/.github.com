#include<stdio.h>
#include<stdlib.h>
//importing another C program in this program
#include"Temp.c"

//defining external storage class

extern int a=6;

int main()
{
    //Storage classes
    
/************Auto class************/
    
    //default class or local variable
    
    auto int n=5;
    printf("%d\n",n);
    
/***********Extern class***********/

        //like global variable declaration
        
        
        //a=5;
        printf("%d\n",a);
        
/************static class***********/

        //remains available till whole program
        
        static int s=7;
        s++;
        printf("%d\n",s);
        printf("%d\n",s);
        
/***********Register class**********/
        
        //stored in CPU (frequently used)
        
        register int num=77;
        printf("%d\n",num);
        
        
}