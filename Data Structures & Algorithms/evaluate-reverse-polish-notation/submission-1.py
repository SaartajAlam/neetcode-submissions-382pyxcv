class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for token in tokens:
            if len(stack) >= 2 and token in operations:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == "+":
                    res = (op2 + op1)
                elif token == "-":
                    res = (op1 - op2)
                elif token == "*":
                    res = (op2 * op1)
                else:
                    res = int(op1 / op2)
                stack.append(res)
            else:
                stack.append(int(token)) 
        return stack[-1]