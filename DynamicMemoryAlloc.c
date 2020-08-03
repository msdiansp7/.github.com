#include<stdio.h>
//library for DynamicMemmoryAlloc
#include<stdlib.h>
#include<string.h>

int main()
{
    int n,i;
    
    //we can allocate memory at runtime of code 
    
    //printf("Enter the no. of times you want to run code : ");
    //scanf("%d",&n);
    scanf("%d",&n);
    
    //defining pointer
    
    //int* point;
    
/*****defining memory allocation*****/
    //point = (int*)malloc(sizeof(int));
    
    /*for(i=0;i<n;i++)
    {
        printf("Enter the number you want to allocate : ");
        scanf("%d\n",&point[i]);
        
    }
    
    for(i=0;i<n;i++)
    {
        printf("%d\n",point[i]);
    }*/
    
    //printf("%d\n",*point);
    //free(point);
    //printf("%d\n",sizeof(point));
    //printf("%d",*point);
    
/****Defining contigious allocation****/
    
    int* points;
    points=(int*)calloc(n,sizeof(int));
    
    /*for(int i=0;i<n;i++)
    {
        printf("%d\n",i);
    }*/
    
/*******Defining Re-allocation*******/
    points=(int*) realloc(points,(n+1)*sizeof(int));
    for(i=0;i<=n;i++)
    {
        printf("%d\n",i);
    }
    
/*******defining free function*******/    //used to free the allocated memory
     
     free(points);
}