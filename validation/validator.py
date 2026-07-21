# Rules:
# - The email must contain "@"
# - The username must be at least 5 characters long

def validate_user(user):

    results = []

    # Email validation
    email_valid = "@" in user["email"]

    if email_valid:
        results.append(("email_format", "PASS", "Valid email"))
    else:
        results.append(("email_format", "FAIL", "Invalid email"))

    # Username validation
    username_valid = len(user["username"]) >= 5

    if username_valid:
        results.append(("username_length", "PASS", "Valid length"))
    else:
        results.append((
    "username_length",
    "FAIL",
    f"Username '{user['username']}' has {len(user['username'])} characters. A minimum of 5 is required."
    ))

    # The user is valid only if all the rules are met
    is_valid = email_valid and username_valid

    return is_valid, results