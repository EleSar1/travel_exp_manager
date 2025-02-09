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

    """
    Displays a summary table of daily expenses for each category, along with the total per category
    and the grand total for all expenses.

    Args:
        expenses_for_category (dict): A dictionary where keys are expense categories and values are lists
                                      containing daily expenses and the total expense for that category.
        grandtotal (float): The total amount spent across all categories.
        travel_days (int): The number of days in the trip, used to format the table header.

    Returns:
        None: The function prints the summary table and the grand total.
    """

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
        print(f"Warning: Your expenses exceed the entered budget by ${grandtotal - budget:.2f}.")
    else:
        print("Good job! You are staying within the set budget.")


def modify_expenses(expenses_for_category: float, travel_days: int):

    category_to_change = ""

    while category_to_change not in expenses_for_category.keys():
        category_to_change = input("Please choose a category between:\nLodging | Meals | Transport | Other\n").strip().capitalize()
        if category_to_change not in expenses_for_category.keys():
            print("Error. This category doesn't exist, please enter a valid category.")

    changing_day = 0

    while changing_day < 1 or changing_day > travel_days:
        try:
            changing_day = int(input(f"Enter the day of change (1-{travel_days}): "))
            if changing_day < 1 or changing_day > travel_days:
                print("Day out of range, please enter a valid day.")
        except ValueError:
            print("Error. Day must be an integer.")
        
    new_expense = -1

    while new_expense < 0:
        try:
            new_expense = float(input(f"Please enter the new expense for day {changing_day}: $"))
            if new_expense < 0:
                print("Expense cannot be negative.")
        except ValueError: 
            print("Error. Please enter a valid number.")
        
    expenses_for_category[category_to_change][changing_day-1] = new_expense

    for category in expenses_for_category.keys():
        if len(expenses_for_category[category]) > travel_days:
            expenses_for_category[category].pop()

    return expenses_for_category


def main():

    # Step 1: Get travel details and initialize expenses
    travel_days, budget = get_travel_details()
    expenses_for_category = initialize_expenses(travel_days)
    
    # Step 2: Collect expenses for each category and day
    expenses_for_category = collect_expenses(travel_days, expenses_for_category)

    # Step 3: Display the expenses and totals before modification
    category_totals = calculate_category_totals(expenses_for_category)
    grandtotal = calculate_grandtotal(category_totals)
    display_totals(category_totals, grandtotal, travel_days)
    check_budget(budget, grandtotal)

    # Step 4: Modify expenses if necessary
    choice = ""
    while choice not in ("Y", "N"):
        choice = input("Do you want to modify any expense? (Y/N): \n").strip().upper()

        if choice not in ("Y", "N"):
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        
        elif choice == "N":
            print("\nGoodbye!")

        
    while choice == "Y":

        modified_expenses = modify_expenses(expenses_for_category, travel_days)

        choice = ""
        while choice not in ("Y", "N"):
            choice = input("Do you want to modify anything else? (Y/N):\n").strip().upper()
            if choice not in ("Y", "N"):
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
            elif choice == "N":
                # Step 5: Recalculate and display the totals after modification
                new_category_totals = calculate_category_totals(modified_expenses)
                new_grandtotal = calculate_grandtotal(new_category_totals)
        
                display_totals(new_category_totals, new_grandtotal, travel_days)
                check_budget(budget, new_grandtotal)

                print("\nGoodbye!")    
            

if __name__ == "__main__":
    main()