/********Preprocessors in C**********/
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define PI 3.14

int main()
{

/********Predefined Macros*********/
        //This prints current file name
    printf("This files's name is %s.\n",__FILE__);
        //This prints current time
    printf("The Current time is %s\n",__TIME__);
        //This prints today's date
    printf("Today's date is %s\n",__DATE__);
        //This prints line number
    printf("This is %d th line.\n",__LINE__);
        //This prints whether the current code is ACSII or not
    printf("ANSI : %d\n",__STDC__);

}