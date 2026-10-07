class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        stack = []

        for t in tokens:
            if t not in ['*', '+', '-', '/']:
                t.append(stack)
            else:
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '/':
                    stack.append(a / b)
                elif t == '*':
                    stack.append(a * b)
        return stack.pop()
            
                
