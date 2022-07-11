class Empty(Exception):
    pass

class MyStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

def postfix_to_infix(postfix_split):
    operator = ['+', '-', '*', '/', '^']
    stack = MyStack()
    infix = []
    postfix = postfix_split.split()
    for i in range(len(postfix)):
        if postfix[i] not in operator:
            stack.push(postfix[i])
        if postfix[i] in operator and len(stack) > 1:
            right = stack.pop()
            left = stack.pop()
            if postfix[i] == '^':
                infix.append("(" + left + '**' + right + ")")
            else:
                infix.append("(" + left + postfix[i] + right + ")")
            stack.push(infix.pop())
    result = str(stack.pop())
    print(result)
    print(eval(result))

# Examples
print("Example 1: 2 20 * 2 / 3 4 + 3 2 ^ * + 6 - 15 +")
postfix_1 = "2 20 * 2 / 3 4 + 3 2 ^ * + 6 - 15 +"
postfix_to_infix(postfix_1)

print('')

print("Example 2: 5.9 5.3 - 7.2 * 1.4 2 ^ +")
postfix_2= "5.9 5.3 - 7.2 * 1.4 2 ^ +"
postfix_to_infix(postfix_2)






