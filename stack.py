class stack:
    def __init__(self):
        self.a=list()

    def push(self,val):
        self.a.append(val)

    def pop(self):
        self.a.pop()

    def top(self):
        return self.a[len(self.a)-1]

    def empty(self):
        # for this case only
        if(len(self.a)==0):
            return False
        return True
