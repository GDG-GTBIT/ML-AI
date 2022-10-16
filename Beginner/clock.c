#include <stdio.h>
#include <windows.h>
#include <time.h>
#include <stdlib.h>
int main()
{
    int h,m,s;
    int d=1000;
    printf("SET TIME :\n");
    scanf("%d %d %d",&h,&m,&s);
    if(h>12||m>59||s>59)
    {
        printf("ERROR:\n");
        exit(0);

    }
    while(1)
    {
        s++;
        if(s>59)
        {
            m++;
            s=0;
        }
        if(m>59)
        {
            h++;
            m=0;
        }
        if(h>12)
        {
            h=1;
        }
        printf("CLOCK :\n");
        printf("%2d:%2d:%2d",h,m,s);
        Sleep(d);
        system("cls");

    }
    return 0;

}
