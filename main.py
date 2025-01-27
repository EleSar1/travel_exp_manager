

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

choice = input("Do you want to modify any expense? Y/N\n").upper()
if choice == "Y":
    category_to_change = input("Please choose a category between\nLodging | Meals | Transport | Other\n").capitalize()
    if category_to_change in expenses_for_category.keys():
        day_to_change = int(input("Please select the day: "))
        if day_to_change > travel_days or day_to_change < 1: 
            print("Error. Day not found.")
        else: 
            new_expense = float(input(f"Please enter the new expense for day {day_to_change}: $"))
            expenses_for_category[category_to_change][day_to_change-1] = new_expense
            expenses_for_category[category_to_change].pop()             #delete the total expense for the selected category
            expenses_for_category[category_to_change].append(sum(expenses_for_category[category_to_change]))
            new_grandtotal = []
            for total_for_category in expenses_for_category.values():
                new_grandtotal.append(total_for_category[-1])
            new_grandtotal = sum(new_grandtotal)
            print(f"New total expenses for:")
            for category, expense in expenses_for_category.items():    
                if expense[-1].is_integer:
                    print(f"{category}: ${int(expense[-1])}")
                else:
                    print(f"{category}: ${expense[-1]:.2f}")
            print(f"Grandtotal: ${new_grandtotal:.2f}")