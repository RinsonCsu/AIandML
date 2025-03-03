print('Meal Charge Callculator')
print('========================\n')

TIP_PERCENT = 18
SALES_TAX_PERCENT = 7

while True:
    try:
        food_charge = float(input('Enter Charge for the food:\n'))
    except Exception as err:
        print("Format Error:", err)
        print("Food Charge entered is not valid")
        continue

    if(food_charge < 0):
        print("Food Charge Cannot be negative") 
        continue
    
    tip = food_charge * TIP_PERCENT/100
    sales_tax = food_charge * SALES_TAX_PERCENT/100
    total = food_charge + tip + sales_tax
            
    print("Charge Details")
    print('==============')
    print("Food Charge   : ${}".format(round(food_charge, 2)))
    print("Tip           : ${}".format(round(tip, 2)))
    print("Sales Tax     : ${}".format(round(sales_tax, 2)))
    print('===================================')
    print("Total Price   : ${}".format(round(total, 2)))        
        
    more_charges_to_enter = input('\nEnter "Y" if more Charge to Enter?\n')
    if (more_charges_to_enter.lower() != "y"):
        break
         
print ('Exiting Calculator!')
