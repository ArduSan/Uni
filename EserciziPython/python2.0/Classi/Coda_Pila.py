class Stack:
    def __init__(self):
        self.List=[]
    def push(self,elem):
        self.List.append(elem)
    def pop(self):
        self.List.pop(len(self.List)-1)
    def top(self):
        print self.List[len(self.List)-1]
    def empty(self):
        if self.List==[]:
            print True
    

