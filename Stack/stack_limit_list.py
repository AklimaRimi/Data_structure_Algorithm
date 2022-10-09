from mimetypes import init


class stack_lim:
    def __init__(self, size):
        self.stack =[]
        self.lim = size
        
    def push(self, value):
        if len(self.stack) >= self.lim :
            print('Stack Overflow')
        else:
            self.stack.append(value)
    def pop(self):
        if  len(self.stack) == 0:
            print('Stack underflow')
        else:
            self.stack.pop()
    def top(self):
        if len(self.stack)>0:
            print(self.stack[-1])
    def size(self):
        print(len(self.stack))
        
        
stack = stack_lim(5)
stack.push('rimi')
stack.push('krimi')
stack.push('bimi')
stack.push('chimi')
stack.push('bimi')
stack.push('chimi')

stack.size()
stack.top()