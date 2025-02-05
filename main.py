from tabulate import tabulate 

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


def initialize_expenses(travel_days: int):
    
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


def collect_expenses(travel_days: int, expenses_for_category: dict):

    """
    Collects daily expenses for each category from user input.  
    Ensures that the input is a valid non-negative number.

    Args:
        travel_days (int)
        expenses_for_category (dict)

    Returns:
        dict: The updated dictionary with collected expenses per day for each category.
    """

    print("Please enter your expenses for the corresponding day and category.")

    for day in range(travel_days):
        print(f"Day {day + 1}")
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


def calculate_category_totals(expenses_for_category: dict):

    """
    Calculates the total expenses for each category by summing all daily expenses.  
    The total is appended as the last element of each category's expense list.

    Args:
        expenses_for_category (dict)

    Returns:
        dict: The updated dictionary with the total expense for each category 
              appended at the end of the corresponding list.
    """

    for expense in expenses_for_category.values():
        expense.append(sum(expense))
    
    return expenses_for_category


def calculate_grandtotal(expenses_for_category: dict):
    """
    Calculates the grand total of all expenses by summing the total expenses  
    for each category.

    Args:
        expenses_for_category (dict)

    Returns:
        float: The grand total of all expenses across all categories.
    """

    grandtotal = [] 

    # Iterate over each category's list and extract the last element (total for that category)
    for total_for_category in expenses_for_category.values():
        grandtotal.append(total_for_category[-1])
    grandtotal = sum(grandtotal)
    
    return grandtotal


def display_totals(expenses_for_category: dict, grandtotal: float, travel_days: int):

    header = ["Category"] + [f"Day {day + 1}" for day in range(travel_days)] + ["Total"]
    table = []

    for category, expenses in expenses_for_category.items():
        formatted_expenses = [f"${int(expense)}" if expense.is_integer() else f"${expense:.2f}" for expense in expenses]
        table.append([category, *formatted_expenses])
    
    print(tabulate(table, headers=header, tablefmt="grid"))

    if grandtotal.is_integer():
        print(f"\nGrandtotal: ${int(grandtotal)}\n")
    else:
        print(f"\nGrandtotal: ${grandtotal:.2f}\n")


def check_budget(budget: float, grandtotal: float):
    """
    Compares the total expenses with the budget and provides feedback.

    Args:
        budget (float): The total budget for the trip.
        grandtotal (float): The total expenses.

    Returns:
        None
    """
    
    if budget < grandtotal:
        print("Warning: Your expenses exceed the entered budget.")
    else:
        print("Good job! You are staying within the set budget.")


def modify_expenses():

    pass


def main():

    pass 


if __name__ == "__main__":
    main()