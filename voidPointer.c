#include<stdio.h>
#include<stdlib.h>

int dangPtr()
{
    int a,b,sum;
    a=7;
    b=8;
    sum=a+b;
    return &sum;
}

int main()
{
    
    
/*******defining a void pointer******/
 
     
    int a=7;
    void* pointr;
    pointr=&a;
    //printing value of address stored in the pointer
    printf("%d\n",*((int*)pointr));
    
/*******defining Null pointer********/

    int* p=NULL;
    printf("%d\n",p);//p is null pointer now
    
/********Dangling pointer**********/
    
            //1.)De-allocation of meomory
    
    int* ptr=(int*)malloc(6 * sizeof(int));
    ptr[0]=6;
    free(ptr);
    printf("%d\n",*ptr);
    
            //2.)function returning global variable
            
     int* dngptr=dangPtr();//dngptr is now dangling pointer
     
             //3.)variable goes out of scope
           
       int* ptr;
         {
             int i=7;
             
             *ptr=&i;
             
         }
         printf("%d\n",*ptr);//ptr is dangling pointer
        
 
     
}