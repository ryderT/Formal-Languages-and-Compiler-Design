%{
    #include <stdio.h>
    #include "scanner.h"
    #include <math.h>
    int lineIndex = 0
%}

digit           [0-9]
nonzerodigit    [1-9]
charsequence    ["]([ _a-zA-Z])*["]
identifier      [a-zA-Z][a-zA-Z0-9]*
constant        {NUMBER}|{charsequence}

%%

"int"                   {printf("reserved word: %s \n", yytext); return inti;}
"float"                   {printf("reserved word: %s \n", yytext); return floati;}
"bool"                  {printf("Reserved word: %s\n", yytext); return booli;}
"string"                {printf("Reserved word: %s\n", yytext); return stringi;}
"readConsole"           {printf("Reserved word: %s\n", yytext); return readi;}
"writeConsole"          {printf("Reserved word: %s\n", yytext); return writei;}
"and"                   {printf("Reserved word: %s\n", yytext); return and;}
"or"                    {printf("Reserved word: %s\n", yytext); return or;}
"while"                 {printf("Reserved word: %s\n", yytext); return whilei;}
"do"                    {printf("Reserved word: %s \n", yytext); return doi;}
"if"                    {printf("Reserved word: %s \n", yytext); return ifi;}
"else"                  {printf("Reserved word: %s\n", yytext); return elsei;}
"+"                     {printf("Operator: %s\n", yytext); return plusi;}
"-"                     {printf("Operator: %s\n", yytext); return minusi;}
"*"                     {printf("Operator: %s\n", yytext); return multiplication;}
"/"                     {printf("Operator: %s\n", yytext); return div;}
"%"                     {printf("Operator: %s\n", yytext); return floatdiv;}
"<"                     {printf("Operator: %s\n", yytext); return less;}
"<="                    {printf("Operator: %s\n", yytext); return lessequal;}
"=="                    {printf("Operator: %s\n", yytext); return equal;}
">="                    {printf("Operator: %s\n", yytext); return greatequal;}
">"                     {printf("Operator: %s\n", yytext); return great;}
"="                     {printf("Separator: %s\n", yytext); return attribution;}
"{"                     {printf("Separator: %s\n", yytext); return openacc;}
"}"                     {printf("Separator: %s\n", yytext); return closeacc;}
"("                     {printf("Separator: %s\n", yytext); return openpara;}
")"                     {printf("Separator: %s\n", yytext); return closepara;}
";"                     {printf("Separator: %s\n", yytext); return semicolon;}
","                     {printf("Separator: %s\n", yytext); return comma;}

[ \t]+          {}
[\n]            {++lineIndex;}
.               {printf("Illegal symbol: %s at line %u", yytext, lineIndex+1); return -1;}  

%%

int mainflex(void){
    return 1;
}
