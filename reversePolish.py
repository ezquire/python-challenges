ops = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b
}

def calc(exp):
    stack = []
    for i in exp:
        if int(i):
            if len(stack) > 1:
                raise TypeError("Invalid RPN Expression")
            stack.append(int(i))
        elif i in ops.keys():
            if len(stack) != 2:
                raise TypeError("Invalid RPN Expression")
            a = stack.pop()
            b = stack.pop()
            stack.append(ops[i](b,a))
            
    return stack[0]
    

rpn = "3,4,-"
# rpn = '1,2,3'
# rpn = "3,4,+,+,2,*,1,+"
# rpn = "1988"

exp = rpn.split(',')

print(calc(exp))