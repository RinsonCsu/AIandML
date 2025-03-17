import calendar

print('\nAverage Rainfall Data')
print('======================\n')

def get_rainfall_for_the_month(month_name, year):
    while True:
        try:
            rainfall = int(input(f"Enter Rainfall in inches for the month of {month_name} for year {year + 1}:\n"))
            if (rainfall >= 0):
                return rainfall
            else:
                print("Please do not enter negative values")
        except Exception as err:
            print(f"Invalid Format: {err}. Please try again")

def get_number_of_years_of_rainfall():
    while True:
        try:
            number_of_years = int(input("Enter the number of years for Rainfall calculation:\n"))
            if (number_of_years > 0):
                    return number_of_years
            else:
                print("Please enter only positive values")
        except Exception as err:
                print(f"Invalid Format: {err}. Please try again")

# Main Logic                
number_of_years = get_number_of_years_of_rainfall()
overall_rainfall_data = {}
for year in range(0, number_of_years):
    rainfall_data_for_the_year = {}
    for month_name in [month for month in calendar.month_name if month]:
        rainfall_data_for_the_year[month_name] = get_rainfall_for_the_month(month_name, year)
    overall_rainfall_data[year] = rainfall_data_for_the_year

total_rainfall_per_month = {}
for month_name in [month for month in calendar.month_name if month]:
    total_rainfall_for_the_month = 0
    for year in overall_rainfall_data:
        total_rainfall_for_the_month += (overall_rainfall_data[year])[month_name]
    total_rainfall_per_month[month_name] = total_rainfall_for_the_month
        
average_rainfall_per_month = {}
for month_name in [month for month in calendar.month_name if month]:
    total_rainfall_for_the_month = 0
    for year in overall_rainfall_data:
        total_rainfall_for_the_month += (overall_rainfall_data[year])[month_name]
    average_rainfall_per_month[month_name] = round(total_rainfall_for_the_month/number_of_years, 2)

total_rainfall = 0
for month in total_rainfall_per_month:
    total_rainfall += total_rainfall_per_month[month]


print(f"\nTotal rainfall for {number_of_years} year(s) = {total_rainfall} inches\n")
print(f"Average rainfall per month during the given {number_of_years} years is as below\n")
print(f"Month        Total Rainfall  Average Rainfall")
print(f"=====        ==============  ================")
for month in average_rainfall_per_month:
    print(f"{month:<13}{total_rainfall_per_month[month]:<16}{average_rainfall_per_month[month]}")
