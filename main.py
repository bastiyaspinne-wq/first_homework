# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_var(5 ** 2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(5 ** 2) # 1 task
print(int((2+4+6)/3)) # 2 task

number1 = int(input("2: "))
number2 = int(input("4: "))
number3 = int(input("6: "))
numbers_sum = number1 + number2 + number3
number_avg = numbers_sum / 3
print(f"The sum of the numbers: {numbers_sum}")
print(f"The average of the numbers: {number_avg}")



user_input = int(input("Input hours and minutes:")) #3 task
hours_and_minutes = divmod(user_input, 60)
hours = total_minutes // 60
minutes = total_minutes % 60
print(hours_and_minutes)

price = int(input('Enter price:'))  # 4 task
discount_percent = int(input('Enter discount percent:'))
discount_amount = price * (discount_percent / 100)
final_price = int(price - discount_amount)
print(final_price)

user_input = int(input("Enter a number: "))  # 5 task
last_digit = user_input % 10
print(last_digit)

length_input = int(input('Enter lengthe :')) # 6 task
width_input = int(input('Enter width :'))
perimeter = length_input + width_input * 2
print(perimeter)

number = int(input("Enter a number: ")) # 7 task
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)





