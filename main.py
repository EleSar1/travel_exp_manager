
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
            travel_days = int(input("How many days will your trip lasts? "))
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


def initialize_expenses():

    pass


def collect_expenses():
    
    pass


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