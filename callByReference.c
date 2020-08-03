#include<stdio.h>

/*void changeValue(int* x,int* y)
{
    int temp;
    temp= *x;
    *x=*y;
    *y=x;
}*/

/*void addSub(int* x,int* y)
{
    int add,sub;
    add=*x+*y;
    *y=*x-*y;
    *x=add;
}*/

  //function taking argument as array
  
/*void func1(int array[])
{
    for(int i=0;i<6;i++)
    {
        printf("%d\n",array[i]);
    }
     //changing value of argument
     
     array[3]=12345;
}*/

    //taking address as an argument

/*void func2(int* pointer)
{
    for(int i=0;i<6;i++)
    {
        printf("%d\n",*(pointer+i));
    }
    *(pointer + 4)=7777;
}*/

int main()
{
    /*int a=15,b=7;
    printf("sum of a & b is %d and subtraction of a & b is %d\n",a,b);*/
    
    //calling function by reference
    
    /*printf("%d & %d\n",a,b);
    changeValue(&a,&b);
    printf("%d & %d\n",a,b);*/
    
    
    
    /*addSub(&a,&b);
    printf("sum of a & b is %d and subtraction of a & b is %d",a,b);*/
    
    
    //Passing arrays as function argument
    
    /*int arr[]={4,6,3,8,9,0};
    func1(arr);
    func1(arr);
    func2(arr);
    func2(arr);*/
}