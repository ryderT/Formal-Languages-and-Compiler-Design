%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token inti 
%token booli 
%token stringi 
%token arrayi 
%token floati 
%token plusi 
%token minusi 
%token multiplication 
%token div 
%token floatdiv 
%token mod 
%token less 
%token great 
%token lessequal 
%token greatequal 
%token equal 
%token not 
%token notequal 
%token readi 
%token writei 
%token ifi 
%token elsei 
%token fori 
%token whilei 
%token doi 
%token openacc 
%token closeacc 
%token openpara 
%token closepara 
%token semicolon 
%token comma 
%token and 
%token or 
%token attribution
%token id
%token cnst

%start program

%%

program: StmtList;

StmtList: Stmt StmtList
        | Stmt;

Stmt: Decl 
    | Ifstmt
    | ForStmt
    | AssignStmt
    | Iostmt;

Decl: Type id semicolon
    | Type id comma Decl;

Type: 
     | floati
     | inti
     | stringi
     | booli;

Ifstmt: ifi openpara Condition closepara openacc StmtList closeacc elsei openacc StmtList closeacc
      | ifi openpara Condition closepara openacc StmtList closeacc;

Condition: Expression Relation Expression and Condition
         | Expression Relation Expression or Condition
         | Expression Relation Expression;

Relation: less
        | lessequal
        | equal
        | great
        | greatequal;

ForStmt: fori ForCondition ForBody;

ForCondition: openpara AssignStmt Condition semicolon cnst closepara;

ForBody: openacc StmtList closeacc;

AssignStmt: id attribution Expression semicolon;

Iostmt: Istmt
      | Ostmt;

Istmt: readi openpara id closepara semicolon;

Ostmt: writei openpara id closepara semicolon;

Param: id | cnst;

Expression: ArithmExpr;

ArithmExpr : term
           | term plusi ArithmExpr
           | term minusi ArithmExpr 
           | term multiplication ArithmExpr 
           | term div ArithmExpr 
           | term floatdiv ArithmExpr
           | term mod ArithmExpr
           | openpara ArithmExpr closepara;

term : id | cnst ;    

%%

yyerror(char *s)
{
  printf("De la yacc:%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1) 
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
    yydebug = 1;
  if ( !yyparse() ) 
    fprintf(stderr,"\t Finish");
}








