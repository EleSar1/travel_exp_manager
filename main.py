
def get_travel_details():
    
    travel_days = 0
    while travel_days < 1:
        try:
            travel_days = int(input("How many days will your trip last? "))
            if travel_days < 1:
                print("The number of days must be at least 1.")
        except ValueError:
            print("Wrong value. Please enter a valid integer.")

    budget = -1
    while budget < 0:
        try:
            budget = float(input("How much is your budget for this trip? $"))
            if budget < 0:
                print("The budget cannot be negative.")
        except ValueError:
            print("Wrong value. Please enter a valid number.")

    return travel_days, budget
            

def initialize_expenses(travel_days):

    expense_for_category = {"Lodging": [0] * travel_days,  
                            "Meals": [0] * travel_days,
                            "Transport": [0] * travel_days,
                            "Other": [0] * travel_days}
    return expense_for_category


def collect_expenses(travel_days, expense_for_category):
    pass


def main():
    travel_days, budget = get_travel_details()


if __name__ == "__main__":
    main()