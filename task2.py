a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=input("Enter the operation +,-,*,/ : ")
if c=='+':
    print("Addition of numbers is :",a+b)
elif c=='-':
    print("Substraction of numbers is :",a-b)
elif c=='*':
    print("Multiplication of numbers is :",a*b)
else:
    print("Division of numbers is :",a/b)
