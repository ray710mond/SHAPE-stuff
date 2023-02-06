def priority(op):
    if op == '+' or op == '-':
        return 1
    if op == '/' or op == '*':
        return 2


def conv2rpn(inf):
    list  = inf.split(" ")
    stack = []
    output = ""
    for i in range (0, len(list)): 
        print(i)
        if list[i] == '(':
            i+=1
            while list[i] != ')':
                if not i in ['+','-','*','/']:
                    output+=list[i]
                    output+=" "
                else:    
                    while len(stack) > 0 and priority(stack[-1]) > priority(i):
                        output += stack.pop()
                        output +=" "
                    stack.append(list[i])
                i+=1
                    
        if not list[i] in ['+','-','*','/']:
            output+=list[i]
            output+=" "
        else:    
            while len(stack) > 0 and priority(stack[-1]) > priority(list[i]):
                output += stack.pop()
                output +=" "
            stack.append(list[i]) 
    while stack:
        output += stack.pop()
        output += " "
    return output


inf = "( 2 + 3 ) * 5"

print(conv2rpn(inf))