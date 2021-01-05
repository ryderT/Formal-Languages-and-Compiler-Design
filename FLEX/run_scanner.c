#include <stdio.h>
#include "scanner.h"

extern int yylex();
extern int linenumber;
extern char* yytext;

int main(void){
    int ntoken;
    ntoken = yylex();
    while(ntoken){
        printf("Token: %d\n", ntoken);
        ntoken = yylex();
    }
    return 0;
}
