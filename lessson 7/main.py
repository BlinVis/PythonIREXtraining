age=17
age_as_str=str(age)
print(age_as_str,"with data type",type(age_as_str))
y=32
x=5.3
result=x+y
print(int(result))
print(f'I am {str(age)} years old')
#
name=input('Hi my name is ')
print('hello',name)
nr1=int(input('enter the first number:'))
nr2=int(input('enter the second number:'))
rezultati=nr1+nr2
print(rezultati)




try:
    result=10/0
    print(result)
except ZeroDivisionError:
    print('You cant divide with 0')
else:
    print('Code was run suksesisht')
finally:
    print('This always runs')
