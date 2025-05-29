def calculate():
    output= '='
    num1=int(input('enter your no.'))
    result=num1
    while True:
        operator=input('enter your operator if done then enter =')
        if operator!='=':
            num2=int(input('enter your no.'))
        if operator=='+':
            result+=num2
        elif operator=='-':
            result-=num2
        elif operator=='*':
            result*=num2
        elif operator=='/':
            result/=num2
        elif operator=='//':
            result//=num2
        elif operator=='^':
            result**=num2
        elif operator=='root':
            result**=1/num2
        elif operator==output:
            print(result)
            break
calculate()
def sum(a,b):
    return a+b
# a=int(input('enter your no.'))
# b=int(input('enter your no.'))
# sum(a,b)
def sub(a,b):
    return a-b
def product(a,b):
    return a*b
def divide(a,b):
    return a/b
def flore_division(a,b):
    return a//b
def exponent(a,b):
    return a**b
def root(a,b):
    return a**(1/b)
def mode(a):
    if a<0:
        a=-a
    return a


