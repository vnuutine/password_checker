# Loop the program until user quits, allowing for multiple password checks.
while True:

    # Get users password as a global variable (string).
    pswd = input("Input your password: (or type 'q' to quit) ")
    
    # Assign a single "q" for the input required to quit the program.
    if pswd == "q":
        break

    # Function to check the length of the string passed as parameter. Returns a boolean value.
    # len() takes the string and turns the length into a integer.
    def pswd_length(password):
        length = len(password)
        if length < 8:
            return False
        else: 
            return True


    # Function for checking if the parameter string contains atleast one digit. Returns a boolean value.
    def is_digit(password):
        digit_found = False

        for c in password:
            if c.isdigit():
                digit_found = True
                break

        if digit_found == True:
            return True
        else:
            return False
        
    # Function for checking if the parameter string contains atleast one uppercase letter. Returns a boolean value.
    def has_uppercase(password):
        upper_case_found = False
        
        for c in password:
            if c.isupper():
                upper_case_found = True
                break
        
        if upper_case_found == True:
            return True
        else: 
            return False
    #  Function for checking if the parameter string contains atleast one lowercase letter. Returns a boolean value.
    def has_lowercase(password):
        lower_case_found = False
        for c in password:
            if c.islower():
                lower_case_found = True
                break
        if lower_case_found == True:
            return True
        else: 
            return False
        

    # Main function collecting the results of the check functions in to a dictionary and printing the password strength.
    # Also loops through the check function results, giving hints from dictionary.
    def main(password):
        results = { "long enough": pswd_length(password),
                    "has digits": is_digit(password),
                    "has uppercase": has_uppercase(password),
                    "has lowercase": has_lowercase(password)}

        hints = {   "long enough": "Your password should be atleast 8 characters long!",
                    "has digits": "Your password should contain atleast one digit!",
                    "has uppercase": "Your password should contain atleast one uppercase letter",
                    "has lowercase": "Your password should contain atleast one lowercase letter"}
        
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
                print("Your password is good")
            case 4:
                print("Your password is very strong!")

        # Loop for giving the correct hints when some checks return false.
        for (key, result) in results.items():
            if result == False:
                print(hints[key])

    main(pswd)

# TODO: 1.	Add a has_symbol(password) check (for characters like !@#$%^&*).
#   	2.	Adjust results, hints, and scoring to handle 5 rules instead of 4.
#   	3.	Refactor the check functions to avoid repeated patterns (without breaking readability).
#   	4.	Move all function definitions outside the while True loop and confirm everything still works.



    