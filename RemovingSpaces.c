#include<stdio.h>
#include<string.h>

void html(char string[])
{
    int i;
    int in=0;
    int index=0;
    for(index=0;index<strlen(string);index++)
    {
    if(string[i]=='<')
    {
        in=0;
        continue;
    }
    else if(string[i]=='>')
    {
        in=1;
        continue;
    }
    while(in==1)
    {
        string[index]=string[i];
    }
    printf("%c",string[index]);
    }
   
}

int main()
{
	
	char str[35]="<h1> This is the heading </h1>";
	printf("%s\n",str);
	html(str);
	
}