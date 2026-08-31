# Building Mini Banking System
# In this project, you will build a simple mini banking system using only the concepts you have learned so far. You will design functions to create accounts, manage balances, perform transactions, and display account summaries.

# Focus on writing clean, well-structured code using functions, lists, dictionaries, loops, and exception handling. Do not use external libraries.

# Project Requirements
# -------------------------------------------------------------------

# Part 1: Simulate a Database

# Create a global list called:

# accounts This list will store all bank accounts.

# Each account should be stored as a dictionary containing: name, balance, transactions

# The transactions field must be a list. Each transaction should be stored as a dictionary containing: type and amount
# -------------------------------------------------------------------

# Part 2: Add Expense Function

# Create a function:

# create_account(name, initial_balance)

# This function must:

# Validate that the initial balance is not negative

# Raise a ValueError if the balance is invalid

# Prevent duplicate account names

# Create a dictionary for the account

# Append it to the accounts list

# Return the created account

# -------------------------------------------------------------------

# Part 3: Deposit Function

# Create a function:

# deposit(name, amount)

# This function must:

# Validate that the amount is greater than 0

# Raise a ValueError if the amount is invalid

# Find the correct account

# Increase the balance

# Add a transaction record with type "Deposit"

# Return the updated balance

# -------------------------------------------------------------------

# Part 4: Withdraw Function

# Create a function:

# withdraw(name, amount)

# This function must:

# Validate that the amount is greater than 0

# Raise a ValueError if the amount is invalid

# Find the correct account

# Ensure sufficient balance before withdrawing

# Raise a ValueError if funds are insufficient

# Decrease the balance

# Add a transaction record with type "Withdrawal"

# Return the updated balance

# -------------------------------------------------------------------


# Part 5: Show Account Summary

# Create a function:

# show_account(name)

# This function must:

# Display the account name

# Display the current balance

# Display all transactions clearly

# -------------------------------------------------------------------

# Part 6: Testing Section

# Add a testing section at the bottom of your script that:

# Creates at least one account

# Performs multiple deposits

# Performs multiple withdrawals

# Attempts an overdraft

# Attempts creating a duplicate account

# Displays the account summary

# -------------------------------------------------------------------

# Final Requirements

# Your solution must:

# Be clean and well structured

# Use readable variable names

# Include comments where necessary to explain your logic

# Make sure to follow best practices writing functions including descriptions.

# Follow proper indentation and formatting

# Avoid unnecessary or duplicated code

# This project is designed to test your understanding of functions, validation logic, exception handling, and structured thinking. If you can build this system confidently and cleanly on your own, you are thinking like a real Python developer.


# accounts = [{"name":"rajesh", "balance":122.45, "transaction":[{"type":"credit|debit", "amount":1000}]}]
accounts = []


def find_account(name:str):
    """
    Check if account exist or not based on name.
    Args:
        name (str): Account holder name.
    Return:
        None: if not found else dict.
    """
    for account in accounts:
        if account['name'].lower() == name.lower():
            return account
    return None
            
def create_account(name:str, initial_balance:float)->dict:
    """
    Create a new account in bank.
    Args:
        name (str): Account holder name
        initial_balance (float): initial balance amount.
    Return:
        list: return the dictionary of new user account.
    """
    if initial_balance<=0:
        raise ValueError("Minimum balance should be greater than zero")
    
    if find_account(name):
        raise ValueError("name is already taken by someone else. Try with other name")
            
    account_details = {
                        "name":name, 
                        "balance":initial_balance,
                        "transaction":[]
                    }
    accounts.append(account_details)
    return account_details


def deposit(name:str, amount:float)->float:
    """
    Save the amount to the correct person account.
    Args:
        name (str): Account holder name.
        amount (float): Amount to deposit in user's account.
    Return:
        float: Total amount in user's account.
    """
    if amount <=0:
        raise ValueError("Amount should be greater than zero.")
    
    user_account = find_account(name)
    
    if not user_account:
        raise ValueError("name is already taken by someone else. Try with other name")
    
    user_account['balance'] +=amount
    user_account['transaction'].append({"type":"Deposit", "amount":amount})
    
    return user_account['balance']


def withdraw(name:str, amount:float)->float:
    """
    Withdraw amount from the given user's account
    Args:
        name (str): Account holder name
        amount (float): amount to withdraw if sufficient balance mantained otherwise raised ValueError
    Return:
        float: if updated successfully otherwise raise valueerror.
    """
    if amount <= 0:
        raise ValueError("Please provide valid amount to withdraw")
    
    user_account = find_account(name)
    if not user_account:
        raise ValueError("name is already taken by someone else. Try with other name")
    
    if user_account['balance'] < amount:
        raise ValueError(f"Ensufficient balance {user_account['balance']} maintained to withdraw {amount} amount..")
    
    user_account['balance'] -= amount
    user_account['transaction'].append({"type":"Withdrawal", "amount":amount})
        
    return user_account['balance']
    

def show_account(name:str)->None:
    """
    Dispay given user name account details.
    Args:
        name (str): A/c holder name
    Return:
        None: if not found else print details..
    """
    user_account = find_account(name)
    if not user_account:
        raise ValueError("name is already taken by someone else. Try with other name")
    
    print(f"{name} Account Details:")
    print(
        f"Account holder name: {user_account['name']}\n"
        f"Current Balance: {user_account['balance']}\n"
    )
    for transaction in user_account['transaction']:
        print(
            f"Type: {transaction['type']}\n"
            f"Amount: {transaction['amount']}\n"
        )
    


# =======================================================================================
# Testing Section
# =======================================================================================
def run_test():
    try:
        create_account("Baraa", 1000.0)
        deposit("Baraa", 200.0)
        withdraw("Baraa", 150.0)
        # withdraw("Baraa", 2000)  # Overdraft test
        # create_account("Baraa", 300)
        create_account("Tom", 4000.0)
        deposit("Tom", 56.67)
        withdraw("Tom", 190.0)
        
    except ValueError as error:
        print(f"Error: {error}")
    except Exception as e:
        print(f"{e}")
    
    show_account("Baraa")
    print(accounts)

    
run_test()