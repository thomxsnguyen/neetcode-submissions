class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        stack = []
        ans = 0
        for t in tokens:
            if t in ['1', '2', '3', '4', '5', '6', '7' ,'8', '9']:
                stack.append(t)
            if t == '+':
                a = stack.pop()
                b = stack.pop()
                ans += b + a
            elif t == '-':
                a = stack.pop()
                b = stack.pop()
                ans += b - a
            elif t == '/':
                a = stack.pop()
                b = stack.pop()
                ans += b // a
            elif t == '*':
                a = stack.pop()
                b = stack.pop()
                ans += b * a
        return ans
                
