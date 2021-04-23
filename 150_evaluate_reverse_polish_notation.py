class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def calculate(symbol):
            top = stack.pop()
            bottom = stack.pop()
            if symbol == "+":
                stack.append(bottom + top)
            elif symbol == "-":
                stack.append(bottom - top)
            elif symbol == "*":
                stack.append(bottom * top)
            elif symbol == "/":
                stack.append(int(bottom / top))
        for token in tokens:
            #print(stack)
            if token == "+" or token == "-" or token == "*" or token == "/":
                calculate(token)
            else:
                stack.append(int(token))
        return stack.pop()