

travel_days = int(input("How many days will your trip last? "))
budget = float(input("How much is your budget for this trip? $"))

expenses_for_category = {"Lodging": [0] * travel_days,  
                         "Meals": [0] * travel_days,
                         "Transport": [0] * travel_days,
                         "Other": [0] * travel_days}



for day in range(travel_days):
    print(f"Day {day + 1}:")
    for category in expenses_for_category.keys():
        expense = input(f"{category}: ")
        expenses_for_category[category][day] = float(expense)  #add the user input to the proper list 

for category in expenses_for_category.keys():
    expenses_for_category[category].append(sum(expenses_for_category[category]))  #add sum of total expenses for category to the lists (values inside the dictionary expenses_for_category)

print('Total expenses for:')
for category, total_for_category in expenses_for_category.items():
    if total_for_category[-1].is_integer():
        print(f'{category}: {int(total_for_category[-1])}')   #if the number is an integer take off the number (0) after the decimal point
    else:
        print(f'{category}: {total_for_category[-1]:.2f}')

grandtotal = [] 
for total_for_category in expenses_for_category.values():
    grandtotal.append(total_for_category[-1])
grandtotal = sum(grandtotal)
if grandtotal.is_integer():
    print(f"Grandtotal: {int(grandtotal)}")
else: 
    print(f"Grandtotal: {grandtotal:.2f}")