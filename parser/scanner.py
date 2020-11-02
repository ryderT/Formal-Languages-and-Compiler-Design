from symbolTable import SymbolTable
from PIF import PIF
import re

class Scanner:
    def __init__(self,filename):
        self.PIF=PIF()
        self.constants=SymbolTable()
        self.identifiers=SymbolTable()
        self.filename=filename
        self.operators=['+', '-', '*', '/', '<', '<=', '=', '>=', '>','==', '&&', '||', '!', '!=','|', '^', "mod", ',']
        self.separators=['[', ']', '{', '}', '(', ')', ';', ' ', ':', ',', '\n', '\t']
        self.wordList=['if','do','while','else','readConsole','writeConsole','for','int','float','bool','array','string']
        self.tokens=[]
        with open("token.in", 'r') as f:
            for line in f:
                self.tokens.append(line.rstrip("\n"))

    def lineAnalysis(self,line):
        lst=[]
        pos = 0  
        while pos < len(line):
            
            if line[pos] == "\"":
                pos2 = pos + 1
                while pos2 < len(line) and line[pos2] != "\"":
                    pos2 += 1
                string_constant = line[pos:pos2+1]
                lst.append(string_constant)
                pos = pos2
            
            elif line[pos] == "\'":
                pos2 = pos + 1
                while pos2 < len(line) and line[pos2] != "\'":
                    pos2 += 1
                string_constant = line[pos:pos2+1]
                lst.append(string_constant)
                pos = pos2
            
            elif line[pos] == " " or line[pos] == "\n" or line[pos] == "\t":
                pass
            
            elif line[pos] in self.separators:
                lst.append(line[pos])
            else:
                if line[pos] in self.operators and pos < len(line) - 1 and line[pos:pos + 2] in self.operators:
                    new_token = line[pos:pos + 2]
                    lst.append(new_token)
                    pos += 1
                elif line[pos] in self.operators: 
                    lst.append(line[pos])
                else:
                    pos2 = pos + 1
                    while pos2 < len(line) and line[pos2] not in self.separators and line[pos2] not in self.operators:
                        pos2 += 1
                    new_token = line[pos:pos2]
                    lst.append(new_token)
                    pos = pos2 - 1

            pos += 1

        return lst

    def read(self):
        lineIndex=0
        with open(self.filename, 'r') as f:
            for line in f:
                #print(line)
                chunks=self.lineAnalysis(line)
                
                for chunk in chunks:
                    if chunk in self.tokens:
                        self.PIF.add(0,chunk)
                    elif chunk in self.separators:
                        self.PIF.add(0,chunk)
                    elif self.isConstant(chunk):
                        if self.constants.search(chunk) is None:
                            self.constants.insert(chunk)
                        pos=self.constants.search(chunk)
                        self.PIF.add(pos,"constant")
                    elif self.isIndentifier(chunk):
                        if self.identifiers.search(chunk) is None:
                            self.identifiers.insert(chunk)
                        pos=self.identifiers.search(chunk)
                        self.PIF.add(pos,"identifier")
                    else:
                        print("Error on line: "+str(lineIndex)+" , error on chunk:" + chunk)
                
                
            else:
                print("eof")
                print(str(self.identifiers))
                print(str(self.constants))
                print(str(self.PIF))
        
    def isIndentifier(self,chunk):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_)*$', chunk) is not None
    def isConstant(self,chunk):
        return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.*\'$|^\".*\"$', chunk) is not None
scan=Scanner("p1.txt")
scan.read()