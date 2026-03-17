# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
continue_calc = 'y'
while continue_calc.lower() in ['y', 'yes']:
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))
        operation = input('operation(+ - * /): ')
        result = None

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print('Division by zero not allowed')
            else: result = num1 / num2
        else: print('Invalid operation')
        if result is not None: print(result)
    except ValueError:
        print("Error: Please enter only numbers, not letters!")
        continue_calc = input("Do you want to continue? (y/n): ")
print("Thank you for using this program")