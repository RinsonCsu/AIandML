print('Addition and Subtraction of two numbers')
print('=======================================\n')

try:
# Being a progamer myself, could not resist not doing handling exception, sorry!
    num1 = float(input('Enter First Number:\n'))
    num2 = float(input('Enter Second Number:\n'))
    print("Sum")
    print(num1, '+', num2, '=', num1 + num2)
    print("Difference")
    print(num1, '-', num2, '=', num1 - num2)
except Exception as err:
    print("Error Encountered. Error Details:", err)
    print("Please run the program again")
