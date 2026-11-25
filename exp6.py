def is_strong_password(pwd):
    has_len = len(pwd) >= 8
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    return has_len and has_upper and has_lower and has_digit


while True:
    user_input = input("Enter a password (or type 'stop' to exit): ")
    if user_input.lower() == "stop":
        print("Program ended.")
        break

    if is_strong_password(user_input):
        print("Result: Strong Password!")
    else:
        print("Result: Weak Password (Must have >=8 chars, uppercase, lowercase, and digit)")
