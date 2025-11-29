# Get users password as a variable
pswd = input("Input your password: ")

# Function to check the length of the parameter string and return a boolean value based on the length.
def pswd_length(password):
    # Take the string length and assign it a variable as integer
    length = len(password)
    # Return a boolean value if string is long enough
    if length < 8:
        return False
    else: 
        return True


# Function for checking if the parameter string contains atleast one digit.
def is_digit(password):
    # Declare a variable for the digit found, default as false.
    digit_found = False
    # Loop through the string and break the loop if a digit is found, setting the variable to true.
    for c in password:
        if c.isdigit():
            digit_found = True
            break
    # Return a boolean value based if there was a digit found in the string.
    if digit_found == True:
        return True
    else:
        return False


def main():
    results = { "long enough": pswd_length(pswd),
                "has digits": is_digit(pswd)}
    
    results = sum(results.values())

    print(results)
    








    




main()





    