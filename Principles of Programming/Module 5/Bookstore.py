BOOK_POINTS_INFO = {0: 0, 2: 5, 4: 15, 6: 30, 8: 60}
print('\nBook Purchase Points Calculator')
print('=================================\n')

def get_number_of_books():
    while True:
            try:
                number_of_books = int(input("Enter the number of books purchased this month:\n"))
                if (number_of_books >= 0):
                        return number_of_books
                else:
                    print("Number should not be negative")
            except Exception as err:
                    print(f"Invalid Format: {err}. Please try again")


number_of_books_purchased = get_number_of_books()
key_selected = 0
for key in BOOK_POINTS_INFO:
    if number_of_books_purchased >= key:
        key_selected = key
    else:
        break

print(f"\nNumber of points awarded for purchasing {number_of_books_purchased} books = {BOOK_POINTS_INFO[key_selected]}")
