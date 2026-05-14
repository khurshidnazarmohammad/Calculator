def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


print("The operations are:")
print("1. Add  2. Subtract  3. Multiply  4. Divide")

selection = input("Enter your operation (1-4): ")

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

if selection == '1':
    print(number1, '+', number2, '=', add(number1, number2))

elif selection == '2':
    print(number1, '-', number2, '=', sub(number1, number2))

elif selection == '3':
    print(number1, '*', number2, '=', mul(number1, number2))

elif selection == '4':
    print(number1, '/', number2, '=', div(number1, number2))

else:
    print("Invalid input")
