class Stack(object):
    def __init__(self):
        self.stack=[]
        self.numberofitems=0
    def isEmpty(self):
        return self.stack==[]
    def push(self,data):
        self.stack.insert(self.numberofitems,data)
        self.numberofitems+=1
        return '{} pushed to stack'.format(data)
    def pop(self):
        self.numberofitems-=1
        data=self.stack.pop(self.numberofitems)
        return '{} pop to stack'.format(data)
    def stacksize(self):
        return len(self.stack)
if __name__=='__main__':
    s=Stack()
    print(s.push(2))
    print(s.push(5))
    print(s.push(7))
    print(s.push(3))

    print(s.pop())
    print(s.pop())
    print('size of stack',s.stacksize())


