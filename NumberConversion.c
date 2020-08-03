#include <stdio.h>
#include<math.h>
#include <string.h>

//Compiler version gcc  6.3.0

int main()
{
  //printf("Hello, Dcoder!");
  //return 0;
  int n,T1,T2,a[10],i,n2,n3,j,B;
  char n1;
  //printf("Enter the value of n : ");
//  scanf("%d",&n);
  printf("From base : ");
  scanf("%d",&T1);
  //printf("To base : ");
//  scanf("%d",&T2);
  if (T1==10){  
  printf("To base : ");
  scanf("%d",&T2);
  printf("Enter the value of n : ");
  scanf("%d",&n);

    if (T2==2){
        
        for(i=0;n>0;i++)    
              {    
                a[i]=n%2;    
                  n=n/2;    
              }    
          printf("\nBinary of Given Number is=");    
          for(i=i-1;i>=0;i--)    
            {    
              printf("%d",a[i]);    
              }    
              
            return 0;
            
        
          }
          if(T2==8){
            for(i=0;n>0;i++)    
              {    
                a[i]=n%8;    
                  n=n/8;    
              }    
          printf("\nOctal of Given Number is=");    
          for(i=i-1;i>=0;i--)    
            {    
              printf("%d",a[i]);    
              }    
              
            return 0;
          }
          if(T2==16){
            char A='A',B='B',C='C',D='D',E='E',F='F';
            for(i=0;n>0;i++)    
              {    
                n1=n%16;
                if(n1==10){
                  a[i]=A;
                }
                else if(n1==11){
                  a[i]=B;
                }
                else if(n1==12){
                  a[i]=C;
                }
                else if(n1==13){
                  a[i]=D;
                }
                else if(n1==14){
                  a[i]=E;
                }
                else if(n1==15){
                  a[i]=F;
                }
                else if(n1==1){
                    a[i]='1';
                }
                 else if(n1==2){
                    a[i]='2';
                }
                else if(n1==3){
                    a[i]='3';
                }
                else if(n1==4){
                    a[i]='4';
                }
                else if(n1==5){
                    a[i]='5';
                }
                else if(n1==6){
                    a[i]='6';
                }
                else if(n1==7){
                    a[i]='7';
                }
                else if(n1==8){
                    a[i]='8';
                }
                else if(n1==9){
                    a[i]='9';
                }
                
                else{
                    a[i]=n1;
                }
               
                  n=n/16;    
              }    
          printf("\nHexadecimal of Given Number is= ");   
          
          for(i=i-1;i>=0;i--){
            
            printf(" %c",a[i]);
          
          }
    }
  }
  if(T1==2)
  {
   int DV=0;
  printf("To base : ");
  scanf("%d",&T2);
  printf("Enter the value of n : ");
  scanf("%d",&a);
  for(i=0;i<10;i++)
          {
              n2=a[i]*pow(2,i);
              DV+=n2;
          }
      if(T2==10)
      {
          printf("%d",DV);
      }
  }
  
}