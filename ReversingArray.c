#include<stdio.h>
#include<string.h>

//function for printing the reverse array 

int revArr(int Arr[])
{
    int i;
    for(i=9;i>=0;i--)
    {
        printf("%d\n",Arr[i]);
    }

}

int main()
{
    int nums[]={1,2,3,4,5,6,7,8,9,0};
    
    //printing array
    
    for(int i=0;i<=9;i++)
    {
        printf("%d\n",nums[i]);
    }
    printf("\nReversing the array : \n\n");
    revArr(nums);
    
}