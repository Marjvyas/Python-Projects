print("-----CALCULATOR-----")
while True:
    a=float(input("Enter the first digit:"))
    b=float(input("Enter the second digit:"))
    op=input("What type of operation you want to perform?(+,-,*,/,%) and q to quite:")
    if op=='+':
        print(a+b)
    elif op=='-':
        print(a-b)
    elif op=='*':
        print(a*b)
    elif op=='/':
        print(a/b)
    elif op=='%':
        print(a%b)
    elif op.lower()=='q':
        break
    else:
        print('Invalid operator...')