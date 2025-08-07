#include <ctype.h>
#include <stdio.h>
#define BUFSIZE 100
char buf[BUFSIZE];
int bufp = 0;


int getch(void){
    return (bufp > 0) ? buf[--bufp] : getchar();
}


void ungetch(int c){
    if (bufp >= BUFSIZE)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}

int getfloat(float *pn)
{
    float frac = 0;
    int c, sign;
    int j = 0
     
    while(isspace(c = getch())); // skipping all the whitespace
     
    if(!isdigit(c) && c != EOF && c != '-' && c != '+'&& c != '.') {
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
    if (c == '.')
        c = getchar();
        for (isdigit(c); c = getch()) { 
            frac = 10.0 * frac + (float) (c - '0');
            ++j 
    }
    *pn += frac/powf(10, j)
    *pn *= sign 
    if (c != EOF)
        ungetch(c);
    return c;
}

int main(int argc, char** argv) {
     
    float r, i;
     
    while((r = getfloat(&i)) != EOF)
        if(r != 0)
            printf("res: %f\n", i);
             
    return 0;
}


