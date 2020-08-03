#include<stdio.h>
#include<string.h>


//defining structures

//giving new name to struct users


/*typedef struct users
{
        int Roll_no;
        char Name[10];
        char Email[20];
 } std;*/

//declaring structures

//struct users u1,u2;

/************Exercise**************/
struct Manage
{
    char Name[20];
    int N;
    int age;
}m,m2,m3;

int main()
{
    scanf("%d\n",&m.N);
    scanf("%d\n",&m2.N);
    scanf("%d\n",&m3.N);
    printf("%d\n",m.N);
    printf("%d\n",m2.N);
    printf("%d\n",m3.N);
    //int a=6;
   /* //struct users u1,u2;
    
    //using new name for struct users as
    std u1,u2;
    
    //assigning values to the structure's content
    
    u1.Roll_no= 165;
    
    //copying strings to the structure's variable
    
    strcpy(u1.Name,"Shubham");
    strcpy(u1.Email,"msdiansp@gmail.com");
    u2.Roll_no = 172;
    strcpy(u2.Name,"Vishwajeet");
    strcpy(u2.Email,"Vishwajeet@gmail.com");
    
    //printing values of structure
    
    printf("%s's roll no. is %d and his email id is %s.\n",u1.Name,u1.Roll_no,u1.Email);
    printf("%s's roll no. is %d and his email id is %s.\n",u2.Name,u2.Roll_no,u2.Email);*/
    
/**********Typedef in c************/
    
    //it is used to give new name(nickname) to datatype for our simplicity
    
/* //defining "ul" name to "unsigned long"
    typedef unsigned long ul;
    ul l1,l2,l3;
    
    typedef int* iP;
    
    iP ptr=&a;
    printf("%x\n",ptr);*/
   
}