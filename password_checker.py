# Password checking utility - Ville Nuutinen - 29.11.2025

# Function to check the length of the string passed as parameter. Returns a boolean value.
# len() takes the string and turns the length into a integer.
def has_min_length(password):
    length = len(password)
    if length < 8:
        return False
    else: 
        return True


# Function for checking if the parameter string contains atleast one digit. Returns a boolean value.
def has_digit(password):
    digit_found = False

    for c in password:
        if c.isdigit():
            digit_found = True
            break

    return digit_found
        
# Function for checking if the parameter string contains atleast one uppercase letter. Returns a boolean value.
def has_uppercase(password):
    upper_case_found = False
        
    for c in password:
        if c.isupper():
            upper_case_found = True
            break
        
    return upper_case_found

#  Function for checking if the parameter string contains atleast one lowercase letter. Returns a boolean value.
def has_lowercase(password):
    lower_case_found = False
        
    for c in password:
        if c.islower():
            lower_case_found = True
            break
        
    return lower_case_found
    
# Function for checking if the parameter string contains atleast one of the symbols in the list. Returns a boolean value.
def has_symbol(password):
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    symbol_found = False
    
    for c in password:
        if c in symbols:
            symbol_found = True
            break
    
    return symbol_found
        

# Main function collecting the results of the check functions in to a dictionary and printing the password strength.
# Also loops through the check function results, giving hints from dictionary.
def check_password(password):
    results = { "long enough": has_min_length(password),
                "has digits": has_digit(password),
                "has uppercase": has_uppercase(password),
                "has lowercase": has_lowercase(password),
                "has symbol": has_symbol(password)}

    hints = {   "long enough": "Your password should be atleast 8 characters long!",
                "has digits": "Your password should contain atleast one digit!",
                "has uppercase": "Your password should contain atleast one uppercase letter",
                "has lowercase": "Your password should contain atleast one lowercase letter",
                "has symbol": "Your password should contain atleast one symbol from !@#$%^&*"}
        
    # Takes the results and sums them to and integer for determining the score.
    score = sum(results.values())

    match score:
        case 0:
            print("Your password can't be accepted!")
        case 1:
            print("Your password is very weak!")
        case 2:
            print("Your password is weak!")
        case 3:
            print("Your password is ok")
        case 4:
            print("Your password is strong!")
        case 5:
            print("Your password is very strong!")

    # Loop for giving the correct hints when some checks return false.
    for (key, result) in results.items():
        if not result:
            print(hints[key])

# Loop the program until user quits, allowing for multiple password checks.
while True:

    # Get users password as a global variable (string).
    pswd = input("Input your password: (or type 'q' to quit) ")
    
    # Assign a single "q" for the input required to quit the program.
    if pswd == "q":
        break

    check_password(pswd)


    