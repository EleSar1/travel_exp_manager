

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


if budget < grandtotal: 
    print("Your expenses exceed the entered budget.")
else: 
    print("You are staying within the set budget!")


choice = input("Do you want to change any expense?  Y/N\n")
if choice == "Y":
    print("Choose the category:")
    category_choice = int(input("Press [1] if you want to change Lodging\n[2] if you want to change Meals\n[3] if you want to change Transport\n[4] if you want to change Other\n. . . "))
    while choice == "Y":
        if category_choice == 1:
            day_to_change = int(input("Please select the day: "))
            if day_to_change > day or day_to_change < 1:
                print("Error.")
            else:
                new_expense = float(input(f"Please enter the new expense for day {day_to_change}: $"))
                expenses_for_category["Lodging"][day_to_change-1] = new_expense
        choice = input("Do you want to change anything else? Y/N\n")
    print(new_expense)
    print(expenses_for_category)
else:
    print("Goodbye!")
