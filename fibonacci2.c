#include <stdio.h>

//Recursive function


/*int fibonacci(int n)
{
    if (n == 1 || n == 2)
    {
        return n - 1;
    }
    else
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}*/

int main()
{
    int f, n;
    scanf("%d", &n);
    f = fibonacci(n);
    printf("%d", f);
}
