# Get users password as a variable
pswd = input("Input your password: ")
# TODO: Create a function to check for the length of the password. And make it return a boolean value. 

# Store passwords length as an interger
length = len(pswd)

# Output feedback on passwords length, limit is 8 characters
if length < 8:
    print("Password is not long enough!")
else: 
    print("Password length is good!")

#TODO: Change the return to boolean values and handle the printing on a main function later.

# Function for checking if the parameter string contains atleast one digit.
def is_digit(password):
    # Declare a variable for the digit check and make it equal to false.
    digit_found = False
    # Loop through every character in the string and change the variable to true if digit is found.
    for c in password:
        if c.isdigit():
            digit_found = True
            break
    # Return the feedback based on if there was a digit found.
    if digit_found == True:
        print("Password contains atleast one digit!")
    else:
        print("Password does not contain any digits!")

     # TODO: Create a function for collecting the values from checks and printing the results to the user
     # Return to the user should be given somehow like "Password is strong" "..very strong" "..poor"
     # And it should give hints on how to make the password more strong if needed. 
        

is_digit(pswd)




    