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
            l.append([chunk1,chunk2])  
        return l

    def isDFA(self):
        transitions=[]
        for t in self.S:
            if t[0] in transitions:
                return False
            transitions.append(t[0])
        return True
    
    def acceptsSequence(self,sequence):
        current=self.q0
        trans={}
        for t in self.S:
            trans[t[0]]=t[1]
        for i in sequence:
            if(current, i) in trans.keys():
                current = trans[(current,i)]
            else:
                return False
        return current in self.F


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
        print("1 - list of states(Q)")
        print("2 - alphabet(Sigma)")
        print("3 - initial state(q0)")
        print("4 - final states(F)")
        print("5 - list of transitions(S)")
        print("6 - isDFA")
        print("7 - acceptsSequence")
        print("0 - exit")
        cmd = input("Enter your command:")
        if cmd == "0":
            break
        elif cmd == "1":
            print(fa.Q,'\n')
        elif cmd == "2":
            print(fa.E,'\n')
        elif cmd == "3":
            print(fa.q0,'\n')
        elif cmd == "4":
            print(fa.F,'\n')
        elif cmd =="6":
            print(fa.isDFA(),'\n')
        elif cmd == "7":
            sequence=input("Enter sequence:")
            print(fa.acceptsSequence(sequence),'\n')
        elif cmd == "5":
            for i in fa.S:
                print(i[0],'->',i[1])
        else:
            print("invalid command")
main()