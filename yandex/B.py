expr = input()
expr = expr.replace(" ", "")
n = len(expr)
stack = []
res, sign = 0, 1


i = 0
while i < n:
    x = expr[i]
    match x:
        case "+" | "-":
            m_counter = 0
            while i < n and expr[i] in {"+", "-"}:
                if expr[i] == "-":
                    m_counter += 1
                i += 1
            sign = -1 if m_counter & 1 else 1
        case _ if x.isdigit():
            num = []
            while i < n and expr[i].isdigit():
                num.append(expr[i])
                i += 1
            res += sign * int("".join(num))

        case "(":
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
            i += 1

        case ")":
            prev_sign = stack.pop()
            prev_res = stack.pop()
            res = prev_res + prev_sign * res
            i += 1

        case _:
            i += 1
        
print(res)
