class FiniteAutomata:
    def __init__(self,filename):
        self.filename=filename
        self.Q,self.E,self.q0,self.F,self.S = self.readFromFile()

    def readFromFile(self):
        with open(self.filename) as f:
            Q = self.parseLine(f.readline())
            E = self.parseLine(f.readline())
            q0 = f.readline().split('=')[1].strip()
            F = self.parseLine(f.readline())
            S = self.getTransitionsFromFile(f)
        
        return Q,E,q0,F,S

    def parseLine(self,line):
        return [chunk.strip() for chunk in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]
    
    def getTransitionsFromFile(self,f):
        f.readline()
        l=[]
        for line in f:
            chunk1=(line[1],line[4])
            chunk2=line[10]
            l.append((chunk1,chunk2))  
        return l
    

    def __str__(self):
        return "Q="+str(self.Q)+\
        " ,\nE="+str(self.E)+\
        " ,\nq0="+str(self.q0)+\
        " ,\nF="+str(self.F)+\
        " ,\nS="+str(self.S)\

def main():   
    fa=FiniteAutomata("FA1.txt")
    #print(str(fa1)) 
    while True:
        print("Commands list:")
        print("1 - for the list of states(Q)")
        print("2 - for the alphabet(Sigma)")
        print("3 - for the initial state(q0)")
        print("4 - for the list of final states(F)")
        print("5 - for the list of transitions(S)")
        print("0 - exit")
        cmd = input("Enter your command:")
        if cmd == "0":
            break
        elif cmd == "1":
            print(fa.Q)
        elif cmd == "2":
            print(fa.E)
        elif cmd == "3":
            print(fa.q0)
        elif cmd == "4":
            print(fa.F)
        elif cmd == "5":
            print(' '.join([' -> '.join([str(part) for part in trans]) for trans in fa.S]))
        else:
            print("invalid command")
main()