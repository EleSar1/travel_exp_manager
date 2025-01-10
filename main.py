

travel_days = int(input("How many days will your trip last? "))
budget = float(input("How much is your budget for this trip? $"))

expenses_for_category = {"Lodging": [0 for list_length in range(travel_days)],
                         "Meals": [0 for list_length in range(travel_days)],
                         "Transport": [0 for list_length in range(travel_days)],
                         "Other": [0 for list_length in range(travel_days)]}


