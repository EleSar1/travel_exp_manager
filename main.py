

travel_days = int(input("How many days will your trip last? "))
budget = float(input("How much is your budget for this trip? $"))

expenses_for_category = {"Lodging": [0] * travel_days,
                         "Meals": [0] * travel_days,
                         "Transport": [0] * travel_days,
                         "Other": [0] * travel_days}



for day in range(travel_days):
    for category in expenses_for_category.keys():
        expense = input(f"{category} day {day+1}: ")
        expenses_for_category[category][day] = float(expense)

        
print(expenses_for_category.items())