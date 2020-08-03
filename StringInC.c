#include<stdio.h>
//importing Library for string 
#include<string.h>

/*void rough()
{
       //rough about string 
       
       for(int i=0;i<strlen(Binary);i++)
    {
        num=Binary[i];
        sum=sum+(num*pow(2,i));
        printf("%d\n",num);
        
    }
    printf("%d\n",sum);
    printf("%d",strlen(Binary));
}*/

int main()
{
    int num,l,sum=0;
    
    //Taking input as a string
    
    char Name[10],Surname[10],fullname[20];
    //char name[]="Shubham";
    printf("Enter  your name : \n");
    gets(Name);
    printf("Enter your surname : \n");
    //scanf("%s",&Binary);
    gets(Surname);//Aliter for taking input
    //printf("%s\n",name);
    //printf("%s",Binary);
    //puts(Binary);//Aliter for printing string
    //rough();
    
/*********Functions in String********/
    
    //To calculate length of string
    
    /*printf("Length of Name is : \n");
    l=strlen(Name);
    printf("%d\n",l);*/
    
    //To concatinate(join) two strings
    
   /*printf("Adding name and surname : \n");
    printf(strcat(Name,Surname));*/
    
    //To reverse the string
    
    /*printf("The reverse of Name is : \n");
    puts(strrev(Name));
    printf(strrev(Name));*/
    
    
    //To copy one string into other
    
    /*printf("\nCopying surname into name : \n");
    strcpy(Name,Surname);
    //printf(strcpy(Name,Surname));
    printf(Name);
    strcpy(fullname,strcat(Name,Surname));
    puts(fullname);*/
    
    //To compare two strings 
    
    /*printf("\nComparing Name and Surname : \n");
    printf(strcmp(Name,Surname));*/
    
}