print('Multiplication and Divisioin of two numbers')
print('=======================================\n')

try:
# Being a progammer myself, could not resist not doing handling exception, sorry!
    num1 = float(input('Enter First Number:\n'))
    num2 = float(input('Enter Second Number:\n'))
    print("Product")
    print(num1, 'X', num2, '=', num1 * num2)
    print("Quotient")
    print(num1, '/', num2, '=', round(num1 / num2,3))
except Exception as err:
    print("Error Encountered. Error Details:", err)
    print("Please run the program again")
