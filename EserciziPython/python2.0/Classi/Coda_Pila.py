class Stack:
    def __init__(self):
        self.List=[]
    def push(self,elem):
        self.List.append(elem)
    def pop(self):
        if len(self.List)>0:
            self.List.pop(len(self.List)-1)
        else:
            print "la lista è vuota non puoi rimuovere altri elementi"
    def top(self):
        print self.List[len(self.List)-1]
    def empty(self):
        if self.List==[]:
            return True
        else:
            return False
    

