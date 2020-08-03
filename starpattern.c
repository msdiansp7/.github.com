#include <stdio.h>

        //By recursive function

/*char starpattern1(int n)
{
    if (n == 1)
    {
        printf("*\n");
    }
    else
    {
        printf("*");
        printf(starpattern1(n-1));
    }
}*/

//By iterative function

    //ascending order
    
        /*void starpattern2(int n)
        {
            for(int i=0;i<n;i++)
            {
              for(int j=0;j<=i;j++)
              {
                  printf("%c",'*');
              }
              printf("\n");
            }
        }*/
        
    //descending order
    
        /*void starpattern3(int n)
        {
            for(int i=n-1;i>=0;i--)
            {
                for(int j=0;j<=i;j++)
                {
                    printf("%c",'*');
                }
                printf("\n");
            }
        }*/

int main()
{
   /* int f1, f2, n;
    printf("Enter the no. of rows : \n");
    scanf("%d", &n);
    //f1=starpattern1(n);
    //printf(f1);
    starpattern1(n);
    //starpattern2(n);
    //starpattern3(n);*/
}