## Evaluate reverse polish notation

def evaluate(rpl):
    list = rpl.split(" ")
    stack = []
    for i in range (0, len(list)):
        if not list[i] in ['+','-','*','/']:
            stack.append(list[i])
        else:
                if list[i] == '+':
                    ans = int(stack[len(stack)-2]) + int(stack[len(stack)-1])
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
                if list[i] == '-':
                    ans = int(stack[len(stack)-2]) - int(stack[len(stack)-1])
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
                if list[i] == '*':
                    ans = int(stack[len(stack)-2]) * int(stack[len(stack)-1])
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
                if list[i] == '/':
                    ans = int(stack[len(stack)-2]) / int(stack[len(stack)-1])
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
    for i in stack:
            return i


rpl = "12 3 - 4 +"

print(evaluate(rpl))

## Convert to reverse polish notation

def priority(op):
    if op == '+' or op == '-':
        return 1
    if op == '/' or op == '*':
        return 2


def conv2rpn(inf):
    list  = inf.split(" ")
    stack = []
    output = ""
    for i in list: 
        if not i in ['+','-','*','/']:
            output+=i
            output+=" "
        else:    
            while len(stack) > 0 and priority(stack[-1]) > priority(i):
                output += stack.pop()
                output +=" "
            stack.append(i) 
    while stack:
        output += stack.pop()
        output += " "
    return output


inf = "2 + 3 * 5"

print(conv2rpn(inf))

print(evaluate(conv2rpn(inf)))