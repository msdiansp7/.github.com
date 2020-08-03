#include<stdio.h>

int main()
{
   // char a;
//    a='7';
//    //printf("%x",26);
//    //printf("%o",9);
//    //printf("%x",101);
//        //pointers
//   /* int* ptra = &a;
//    printf("%x\n",ptra);
//    printf("%x\n",*ptra);
//    printf("%x\n",&a);
//    printf("%d\n",a);
//    printf("%d",*ptra);*/
//    int* ptra = &a;
//    printf("%c\n",a);
//    printf("%x\n",*ptra);
//    printf("%c\n",*ptra);

    char a[]={1,2,3,'a','b','d',7,8};
    char* ptr = &a[6];
    printf("%d",&ptr);
}