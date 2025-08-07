#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#define BUFSIZE 100
char buf[BUFSIZE];
int bufp = 0;
// SIZE = 64;

int getch(void){
    return (bufp > 0) ? buf[--bufp] : getchar();
}


void ungetch(int c){
    if (bufp >= BUFSIZE)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}

int getint(int *pn) {
    int c, sign;
     
    while(isspace(c = getch()));
     
    if(!isdigit(c) && c != EOF && c != '-' && c != '+') {
        ungetch(c);
        return 0;
    }
     
    sign = (c == '-')?-1:1;
    if(c == '+' || c == '-')
        c = getch();
         
    *pn = 0;
    while(isdigit(c)) {
        *pn = (*pn * 10) + (c - '0');
        c = getch();
    }
     
    *pn *= sign;
     
    if(c != EOF)
        ungetch(c);
 
 
    return c;
}
 
 
int main(int argc, char** argv) {
     
    int r, i;
     
    while((r = getint(&i)) != EOF)
        if(r != 0)
            printf("res: %d\n", i);
             
    return 0;
}



