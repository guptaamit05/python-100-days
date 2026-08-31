# Building an Expense Tracking System
# In this project, you will build a simple expense tracking system using only the concepts you have learned so far. You will design functions to add, store, analyze, and summarize expenses.

# Before you start, try to solve this project completely on your own. Do not immediately check the solution. Only review the solution if you truly struggle after making a serious attempt. Avoid using AI tools for this task. The goal is to strengthen your thinking and problem-solving skills.

# Project Requirements
# -----------------------------------------------------------------------------------------------------

# Part 1: Simulate a Database

# Create a global list called:

# expenses This list will store all expense entries.

# Each expense should be stored as a dictionary containing: amount, category, description


# -----------------------------------------------------------------------------------------------------
# Part 2: Add Expense Function

# Create a function:

# add_expense(amount, category, description)

# This function must:

# Validate that amount is greater than 0

# Raise a ValueError if the amount is invalid

# Create a dictionary for the expense

# Append it to the expenses list

# Return the created expense


# -----------------------------------------------------------------------------------------------------
# Part 3: Calculate Total Expenses

# Create a function:

# calculate_total_expenses()

# This function must:

# Loop through all expenses

# Calculate the total amount

# Return the total


# -----------------------------------------------------------------------------------------------------
# Part 4: Calculate Total by Category

# Create a function:

# calculate_total_by_category(category)

# This function must:

# Loop through expenses

# Calculate the total only for the given category

# Return the total

# -----------------------------------------------------------------------------------------------------

# Part 5: Show All Expenses

# Create a function:

# show_expenses()

# This function must display all stored expenses clearly
# -----------------------------------------------------------------------------------------------------
# Part 6: Testing Section

# Add a testing section at the bottom of your script that:

# Adds multiple expenses

# Includes at least one invalid expense

# Prints total expenses

# Prints total for a specific category

# Displays all stored expenses


# -----------------------------------------------------------------------------------------------------

# Final Requirements

# Your solution must:

# Be clean and well structured

# Use readable variable names

# Include comments where necessary to explain your logic

# Make sure to follow best practices writing functions including descriptions.

# Follow proper indentation and formatting

# Avoid unnecessary or duplicated code

# This project is designed to test your understanding of functions, validation logic, exception handling, and structured thinking. If you can build this system confidently and cleanly on your own, you are thinking like a real Python developer.

# =================================================================================
# expenses = [{"amount":1000, "category":"clothes", "description":"some description of item"}]
expenses = []


# =================================================================================
# Add Expense.
# =================================================================================
def add_expense(amount:float, category:str, description:str)->dict:
    """"
    Create the expense list of dictionary.
    Return:
        dict: dictionary of amount, cateogry and description.
    Raise:
        ValueError: if validation fails.
    Args:
        amount (float): Amount of the item.
        category (str): Category of the item.
        description (str): Description of the item
    """
    if amount<0:
        raise ValueError("amount field should be greater than zero(0)")
    expense_dict = {"amount":float(amount), "category":category, "description":description}
    expenses.append(expense_dict)
    return expenses

# =================================================================================
# Calculate total expense
# =================================================================================
def calculate_total_expenses()->float:
    """"
    Calculate the total expenses based on amount key.
    Args:
        None
    Return:
        float: return Total expenses (based on amount key). 
    """
    return sum(amount['amount'] for amount in expenses)


# =================================================================================
# Calculate total expenses by a category.
# =================================================================================
def calculate_total_by_category(category:str)->float:
    """
    Calculate the total expenses based on category.
    Args:
        category (str): for which category we need to calculate total expenses.
    Return:
        float: Total amount based on category.
    """
    return sum(expense['amount'] for expense in expenses if expense['category'].lower()==category.lower())


# =================================================================================
# Return All expenses..
# =================================================================================
def show_expenses()->None:
    """
    It will return expenses list.
    Args:
        None
    Return:
        dict: list of dictionary of expenses.
    """
    if not expenses:
        print("No expenses found!")
        return
    print("All Expenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index} {expense['category']}-"
            f"{expense['description']} : ${expense['amount']}"
        )

# =================================================================================
# Testing Section
# =================================================================================
def run_test():
    '''
    Run the application by passing random dictionary.
    
    '''
    expense_list = [
        {"amount":100, "category":"A","description":"A expense desc"},
        {"amount":150, "category":"B","description":"BBBB expense desc"},
        {"amount":180, "category":"V","description":"VVV expense desc"},
        {"amount":120, "category":"A","description":"A expense desc"}
        ]
    try:
        for expense in expense_list:
            add_expense(expense['amount'], expense['category'], expense['description'])
    except ValueError as error:
            print(f"Validaton Error: {error}")
    except Exception as e:
        print(f"Error: {e}")
            
    print(f"Total Expenses: {calculate_total_expenses()}")
    print(f"Total Expenses by Category A: {calculate_total_by_category("A")}")
    show_expenses()
    
        


run_test()