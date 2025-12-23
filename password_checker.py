"""
Password strength checking utility.

Evaluates a password against a small set of rules and provides
a strength classification along with actionable feedback.
"""


# Approved non-alphanumeric symbols allowed in passwords
SYMBOLS = {"!", "@", "#", "$", "%", "^", "&", "*"}


def has_min_length(password):
    return len(password) >= 8


def has_digit(password):
    return any(c.isdigit() for c in password)
        

def has_uppercase(password):
    return any(c.isupper() for c in password)


def has_lowercase(password):
    return any(c.islower() for c in password)
    

def has_symbol(password):
    return any(c in SYMBOLS for c in password)

# Evaluate password strength and return classification and feedback.
# Strength is determined by how many individual rules are satisfied.
def analyze_password(password):
    results = {
        "long enough": has_min_length(password),
        "has digits": has_digit(password),
        "has uppercase": has_uppercase(password),
        "has lowercase": has_lowercase(password),
        "has symbol": has_symbol(password),
    }
    # Aggregate rule results into a simple numeric score 
    score = sum(results.values())
    
    failed_rules = [key for key, value in results.items() if not value]
    
    match score:
        case 0:
            return score, "Very weak", failed_rules
        case 1:
            return score, "Very weak", failed_rules
        case 2: 
            return score, "Weak", failed_rules
        case 3:
            return score, "Ok", failed_rules
        case 4:
            return score, "Strong", failed_rules
        case 5:
            return score, "Very strong", failed_rules

# TODO: Refactor to print the strength, missing rules, score and hints.
def print_report(result):

    hints = {
        "long enough": "Your password should be atleast 8 characters long!",
        "has digits": "Your password should contain atleast one digit!",
        "has uppercase": "Your password should contain atleast one uppercase letter",
        "has lowercase": "Your password should contain atleast one lowercase letter",
        "has symbol": "Your password should contain atleast one symbol from !@#$%^&*",
    }


    # Emit hints for any rules that failed
    for key, result in results.items():
        if not result:
            print(hints[key])


# Interactive loop allowing repeated password checks
while True:
    pswd = input("Input your password: (or type 'q' to quit) ")
    
    if pswd == "q":
        break

    result = analyze_password(pswd)
    
    print_report(result)