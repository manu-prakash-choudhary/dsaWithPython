for t in range(int(input())):

    def condition_check(postfix):
        if len(stack) == 1:
            return True
        elif ( operators.index(infix[i]) - operators.index(stack[-1])) >=2 :
            return True
        
        else:
            postfix+=stack[-1]
            stack.pop(-1)
            return condition_check(postfix)

    n = int(input())
    infix = str(input()).strip() 
    postfix = ""
    stack = ['(']
    operators = ['(', '_' ,'+','-','*','/','__','^' ]

    for i in range(len(infix)):
        if infix[i] in operators:
            if infix[i] == '(':
                stack.append(infix[i])
            elif ( operators.index(infix[i]) - operators.index(stack[-1])) >=2 :
                stack.append(infix[i])
            else : 
                postfix += stack[-1]
                stack.pop(-1)
                if condition_check(postfix):    
                    stack.append(infix[i])
        elif infix[i] == ')':
            j=-1
            while stack[j] != '(':
                postfix += stack[j]
                stack.pop(-1)
            stack.pop(-1)  
        else:
            postfix += infix[i]
    while stack[-1] != '(':
                postfix += stack[-1]
                stack.pop(-1)
    print(postfix,end='')