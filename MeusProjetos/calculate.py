print('Hello, welcome to my calculator!')
Operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
N1 = int(input("Please enter first number"))
N2 = int(input("Please enter second number"))
if Operation == '+':
    Result = N1+N2
elif Operation == '-':
    Result = N1-N2
elif Operation == '/':
    Result = N1/N2
elif Operation == '/':
    Result = N1/N2
elif Operation == '*':
    Result = N1*N2
else:
    print("This calculator can not do this type of operation, try again '-' ")

print("The result of the two given numbers is", Result)
