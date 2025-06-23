num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
user_choice = int(input('Enter your choice: '))
if user_choice == 1:
    total = num1 + num2
    print(f'Total of {num1} + {num2} = {total}')
elif user_choice == 2:
    total = num1 * num2
    print(f'Total of {num1} * {num2} = {total}')
elif user_choice == 3:
    total = num1 / num2
    print(f'Total of {num1} / {num2} = {total}')
elif user_choice == 4:
    total = num1 - num2
    print(f'Total of {num1} - {num2} = {total}')
    print('Done')