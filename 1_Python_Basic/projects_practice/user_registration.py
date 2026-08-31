# Part 1: Simulate a Database

# Create two global lists:

# registered_users list will store successfully registered users.

# failed_registrations list will store information about failed registration attempts.

# -----------------------------------------------------------------------------------------------------------

# Part 2: Create Validation Functions

# You must create the following three functions:

# validate_name(name)
# The name must contain at least 3 characters.
# Return True if the name is valid, otherwise return False.

# validate_email(email)
# The email must contain both "@" and ".".
# Return True if the email format is valid, otherwise return False.

# validate_password(password)
# The password must meet all of the following conditions:
# At least 8 characters long
# Contains at least one uppercase letter
# Contains at least one digit
# Return True if the password is valid, otherwise return False.

# -----------------------------------------------------------------------------------------------------------

# Part 3: Create a Main Validation Function

# Create an orchestrator function called validate_user_data(name, email, password)

# This function must:

# Call the three validation functions you created

# Raise a ValueError with a clear and descriptive message if any validation fails

# Return True if all validations pass successfully

# -----------------------------------------------------------------------------------------------------------

# Part 4: Create the Registration Function

# Create a function called create_user_account(name, email, password)

# This function must:

# Call validate_user_data() to validate the inputs.

# Check whether the email already exists in the registered_users list.

# If a duplicate email is found, raise a ValueError.

# If validation passes and the email is not duplicated:

# Create a dictionary containing name, email, password, and a status set to "active".

# Append the dictionary to registered_users.

# Return the created user dictionary.

# If any error occurs during validation or duplicate checking:

# Catch the ValueError.

# Store a dictionary inside failed_registrations containing the email and the error message.

# Return None.

# -----------------------------------------------------------------------------------------------------------

# Part 5: Testing Your Implementation

# After completing your solution, add a simple testing section at the bottom of your script.

# Test the following cases:

# A valid registration

# A duplicate email

# An invalid name

# An invalid email

# A weak password

# For each case:

# Call create_user_account()

# Print the result

# Print the final contents of registered_users

# Print the final contents of failed_registrations

# The goal is to clearly demonstrate how your system behaves in both successful and failed scenarios.

# -----------------------------------------------------------------------------------------------------------

# Final Requirements

# Your solution must:

# Be clean and well structured

# Use readable variable names

# Include comments where necessary to explain your logic

# Make sure to follow best practices writing functions including descriptions.

# Follow proper indentation and formatting

# Avoid unnecessary or duplicated code

# This project is designed to test your understanding of functions, validation logic, exception handling, and structured thinking. If you can build this system confidently and cleanly on your own, you are thinking like a real Python developer



registered_users = []
failed_registrations=[]

# ==========================================================
# Validation functions
# ==========================================================
def validate_name(name:str)->bool:
    """
    Validate that the name at least contains 3 charecters.
    
    Args:
        name (str): The user's name.
        
    Return:
        bool: True if valid otherwise False.
    """    
    return len(name.strip())>3

def validate_email(email:str)->bool:
    """"
    Valide that the email contains both "@" and "."
    
    Args:
        email (str) : The valid email address.
        
    Return:
        bool: True if valid otherwise False.
    """
    return "@" in email and "." in email


def validate_password(password:str)->bool:
    """
    validate password based one defined rules.
    
    Args:
        password (str): the password.
        
    Return:
        bool: True if valid otherwise False.
        
    Rules:
        At least 8 char long.
        Contains at least one uppercase letter.
        Contains at least one digit.
    """
    if len(password<8):
        return False
    
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_uppercase and has_digit

# ==========================================================
# Orchestrator validation function.
# ==========================================================
def validate_user_data(name:str, email:str, password:str)->None:
    """
    validate all the fields.
    
    Args:
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.
        
    Return:
        None
        
    Raise:
        ValueError: if any validation failed.
    """
    
    if not validate_name(name):
        raise ValueError("validation failed of name")
    if not validate_email(email):
        raise ValueError("validation failed of email")
    if not validate_password(password):
        raise ValueError("validation failed of Password")


# ==========================================================
# Registration Function.
# ==========================================================
def create_user_account(name:str,email:str,password:str):
    """
    Create a new user account after validate.
    
    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.
        
    Return:
        None: if registration fails.
        Dict: User dictionary if registration succeed.
    
    Raise:
        ValueError: raised error if duplicate or validation failed.
    """
    
    try:
        validate_user_data(name, email, password)

        for user in registered_users:
            if email in user.values():
                raise ValueError("email alread exist. Please try with different email")

        new_user = {
                    "name":name,
                    "email":email,
                    "password":password, 
                    "status":"active"
                }    
        registered_users.append(new_user)
        return new_user
    
    except ValueError as e:
        failed_registrations.append(
            {"email":email, "message":str(e)}
        )
        return None
    
    
# ==========================================================
# Testing Section.
# ==========================================================
create_user_account("omkar", 'hari@gmail.com', '234542234')
create_user_account("satish", 'hari@gmail.com', '456444565')
print(registered_users)
print(failed_registrations)
