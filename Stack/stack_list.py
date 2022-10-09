class stack_list:
    def __init__(self):
        self.stack = []
        
    def push(self,value):
        self.stack.append(value)
        
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            return 'A value popped'
        else:
            return 'The stack is empty'
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 'Stack is empty'
    def value(self):
        return len(self.stack)
    
stack = stack_list()

print(stack.value())
print(stack.pop())
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.top())

            
    