# 10799
# 자료구조 - 스택

class Stack():
    def __init__(self):
        self.stack = []
        self.stick = 0
        self.piece = 0
    
    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False

    def push(self, data):  # '(' 입력시
        if not self.isEmpty():
            if self.top() == '(':
                self.stick += 1
        
        self.stack.append(data)
        
        
    def pop(self):  # ')' 입력시
        if self.top() == '(':
            self.piece += self.stick
        else:
            self.stick -= 1
            self.piece += 1

        self.stack.append(')')

    def top(self):
        return self.stack[-1]


ps = input()


# sol1) class 없이 구현
stick = 0
piece = 0

for i in range(1, len(ps)):
    if ps[i-1] == '(':
        if ps[i] == ')':
            piece += stick
        else:
            stick += 1
    elif ps[i] == ')':
        stick -= 1
        piece += 1

print(piece)

# sol2) class(Stack)로 구현

myStack = Stack()

for x in ps:
    if x == '(':
        myStack.push(x)
    else:
        myStack.pop()

print(myStack.piece)