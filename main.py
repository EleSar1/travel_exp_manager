
def get_travel_details():
    
    """
    Prompts the user to input the number of travel days and the total budget.  
    Ensures valid input by handling errors and enforcing positive values.

    Returns:
        tuple: (int, float)  
        - travel_days: The number of days for the trip (must be at least 1).  
        - budget: The total budget for the trip (must be non-negative).  
    """

    travel_days = 0
     # Loop continues until the user enters a valid number for the number of travel days
    while travel_days < 1:
        try: 
            travel_days = int(input("How many days will your trip last? "))
            if travel_days < 1:
                print("The number of days must be at least 1.")
        except ValueError:
            print("Wrong value. Please enter a valid integer.")

    budget = -1
    # Loop continues until the user enters a valid value for the budget
    while budget < 0:
        try:
            budget = float(input("How much is your budget for this trip? $"))
            if budget < 0:
                print("The budget cannot be negative.")         
        except ValueError:
            print("Wrong value. Please enter a valid number.")
    
    return travel_days, budget


def initialize_expenses(travel_days):
    
    """
    Initializes a dictionary to store travel expenses for different categories.  
    Each category will have a list of zeros, one for each travel day.

    Args:
        travel_days (int): The number of days for the trip.

    Returns:
        dict: A dictionary where keys are expense categories  
              ("Lodging", "Meals", "Transport", "Other")  
              and values are lists of zeros with a length equal to travel_days.
    """

    expenses_for_category = {"Lodging": [0] * travel_days,  
                         "Meals": [0] * travel_days,
                         "Transport": [0] * travel_days,
                         "Other": [0] * travel_days}

    return expenses_for_category


def collect_expenses(travel_days, expenses_for_category):

    """
    Collects daily expenses for each category from user input.  
    Ensures that the input is a valid non-negative number.

    Args:
        travel_days (int)
        expenses_for_category (dict)

    Returns:
        dict: The updated dictionary with collected expenses per day for each category.
    """

    for day in range(travel_days):
        print("Please enter your expenses for the corresponding day and category.")
        print(f"Day {day + 1}")
        # Loop through each category to get the expense for that day
        for category, empty_expense in expenses_for_category.items():
            expense = -1
            while expense < 0:
                try:
                    expense = float(input(f"{category}: $"))
                    if expense < 0:
                        print("The expense cannot be negative.")
                except ValueError:
                    print("Wrong value. Please insert a valid number.")
            # Store the entered expense in the correct position for the current day
            empty_expense[day] = expense
    
    return expenses_for_category


def calculate_category_totals():
    
    pass


def calculate_grandtotal():
    
    pass


def display_totals():

    pass


def check_budget():

    pass


def modify_expenses():

    pass


def main():
    
    pass


if __name__ == "__main__":
    main()