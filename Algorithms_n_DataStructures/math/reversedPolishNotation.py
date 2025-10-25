from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []
        for x in tokens:
            if x in operators:
                b, a = stack.pop(), stack.pop()
                match x:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        sign = 1 if (a > 0) == (b > 0) else -1
                        stack.append(sign * (abs(a) // abs(b)))
            else:
                stack.append(int(x))

        return stack.pop()


print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
