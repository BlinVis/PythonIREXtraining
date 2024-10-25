def my_func(num1,num2,operator):
    if operator=='*':
        return(int(num1) * int(num2))
    elif operator=='+':
        return(int(num1) + int(num2))
    elif operator=='-':
        return(int(num1) - int(num2))
    elif operator=='/':
        if int(num2) == 0:
            raise ZeroDivisionError('you cant divide with 0')
        else:return(int(num1) / int(num2))
    else:
        raise ValueError('Invalid operator')

num1,num2=float(input('enter the first number:')),float(input('enter the second number:'))
operator1=input('please choose an operator:')
result=my_func(num1,num2,operator1)
print(result)


