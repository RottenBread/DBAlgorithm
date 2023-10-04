from Stack import Stack

def precedence (op):
    if op == "(" or "}":
        return 0
    elif op == "+" or "-":
        return 1
    elif op == "*" or "/":
        return 2
    else:
        return -1

def Infix2Postfix (expr):
    s = Stack()
    output = []
    for term in expr:
        if term in "(":
            s.push("(")
        elif term in ")":
            while not s.isEmpty():
                op = s.pop()
                if op == "(":
                    break
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)
        
    while not s.isEmpty():
        output.append(s.pop())

    return output

infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
postfix1 = Infix2Postfix(infix1)

print(postfix1)