# repl/repl.py
while True:
    user_input = input('[advanced calculator] What operation would you like to do today? ')
    if user_input == 'exit':
        print('goodbye!')
        break

    if user_input == 'add':
        num1 = int(input('enter first number: '))
        num2 = int(input('enter second number: '))
        print("the answer is " +str(int(num1) + int(num2)))
    elif user_input == 'subtract':
        num1 = int(input('enter first number: '))
        num2 = int(input('enter second number: '))
        print("the answer is " +str(int(num1) - int(num2)))
    elif user_input == 'multiply':
        num1 = int(input('enter first number: '))
        num2 = int(input('enter second number: '))
        print("the answer is " +str(int(num1) * int(num2)))
    elif user_input == 'divide':
        num1 = int(input('enter first number: '))
        num2 = int(input('enter second number: '))
        print("the answer is " +str(int(num1) / int(num2)))
else:
    print("invalid input")

    