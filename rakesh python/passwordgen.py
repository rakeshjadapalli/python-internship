import secrets
import string

def is_strong_password(password, min_length=8):
    if len(password) < min_length:
        return False, "Password must be at least {} characters long.".format(min_length)
    if not any(char.islower() for char in password):
        return False, "Password must include at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return False, "Password must include at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must include at least one number."
    if not any(char in string.punctuation for char in password):
        return False, "Password must include at least one special character (!@#$%^&* etc.)."
    
    return True, "Password is strong."

def generate_strong_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_chars = lower + upper + digits + special
    password = (
        secrets.choice(lower)
        + secrets.choice(upper)
        + secrets.choice(digits)
        + secrets.choice(special)
    )
    
    password += ''.join(secrets.choice(all_chars) for _ in range(length - 4))
    
    return ''.join(secrets.SystemRandom().sample(password, len(password))) 

def get_user_password():
    while True:
        password = input("Enter your password : ").strip()
        print("🔹 You entered:", password)
        
        is_valid, message = is_strong_password(password)
        if is_valid:
            print("✅ Your password is strong!")
            return password
        else:
            print("⚠️", message)
            print("🔁 Please re-enter a strong password.")


if __name__ == "__main__":
    user_password=get_user_password()
    print("password created successfully")