#include<stdio.h>

int main(){
    /*int i=1;
    printf("%20.d\n",i);
    printf("%17.d      %d\n",i,i+1);
    printf("%14.d      %d      %d\n",i,i+1,i+2);
    printf("%11.d%6.d%7.d%8.d\n",i,i+1,i+2,i+3);*/
    
    int i,n,j;
    printf("Enter any number : ");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        for(j=i;j<n;j++){
            printf("  ");
        }
        for(j=1;j<=i;j++){
            printf("%d",j);
            printf("   ");
            
        }
        printf("\n");
    }
}