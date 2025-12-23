"""
Password strength checking utility.
Evaluates a password against a small set of rules and provides
a strength classification along with actionable feedback.
"""

import sys

# Approved non-alphanumeric symbols allowed in passwords
SYMBOLS = {"!", "@", "#", "$", "%", "^", "&", "*"}

HINTS = {
    "long enough": "Your password should be atleast 8 characters long!",
    "has digits": "Your password should contain atleast one digit!",
    "has uppercase": "Your password should contain atleast one uppercase letter",
    "has lowercase": "Your password should contain atleast one lowercase letter",
    "has symbol": "Your password should contain atleast one symbol from !@#$%^&*",
}


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


# Return (score, strength_label, failed_rule_keys) for the given password.
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
        case 0 | 1:
            return score, "Very weak", failed_rules
        case 2: 
            return score, "Weak", failed_rules
        case 3:
            return score, "OK", failed_rules
        case 4:
            return score, "Strong", failed_rules
        case 5:
            return score, "Very strong", failed_rules


def print_report(result):
    
    score, strength, failed_rules = result

    print("Password score (0-5):", score)
    print("Password strength:", strength)
    
    if failed_rules:
        print("Missing rules:")
        for key in failed_rules:
            print("-", HINTS[key])


def main():
    
    argc = len(sys.argv)
    
    if argc !=  2:
        print("Usage: python password_checker.py <password>")
        print("Example: python password_checker.py 'MyPassword123!'")
        return
    
    result = analyze_password(sys.argv[1])
    print_report(result)


if __name__ == "__main__":
    main()