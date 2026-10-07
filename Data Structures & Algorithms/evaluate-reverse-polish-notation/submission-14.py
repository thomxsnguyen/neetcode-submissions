class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ['*', '+', '-', '/']:
                stack.append(t)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == '+':
                    stack.append(b + a)
                elif t == '-':
                    stack.append(b - a)
                elif t == '/':
                    stack.append(int(b / a))
                elif t == '*':
                    stack.append(b * a)

        return stack.pop()