Choice = " "
while Choice != '5':
    print("1. Addition ")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division ")
    print("5. Exit the Progarm ")
    Choice = str(input("Enter the Operation: "))
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))
    Operator = " "
    match Choice:
        case '+': Operator ='+'
        case '-': Operator = '-' 
        case '*': Operator = '*'
        case '/': Operator = '/'
        case '5': Choice = 5
    if Operator == '+':
        print(num1+num2)
    elif Operator == '-':
        print(num1-num2)
    elif Operator == '*':
        print(num1*num2)
    elif Operator == '/':
        if num1 == 0:
            print("Invial number. Division is not posible")   
        else:
            print(num1/num2)           

            
