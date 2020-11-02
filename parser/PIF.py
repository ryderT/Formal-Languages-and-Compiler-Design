class PIF:
    def __init__(self):
        self.content=[]
    def __str__(self):
        result=""
        for i in self.content:
            result += str(i)+'\n'
        return result
    def add(self, id, chunk):
        self.content.append(str([id,str(chunk)]))
    