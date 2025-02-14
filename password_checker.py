import re

#password strength check condition:
#minimum 8 characters, at least one uppercase letter, one lowercase letter, one number and one special character

def check_password_strength(password):
    if len(password) < 8:
       return "Password must be at least 8 characters long"

    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number" 
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"

    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    
    if not re.search(r'''[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]''',password):
        return "Password must contain at least one special character"

    return "Password is strong"

def main():
    while True:
        password = input("Enter password: ")
        if password == "exit":
            print("Exiting...")
            break
        else:
            print(check_password_strength(password))

if __name__ == "__main__":
    main()
