import msvcrt
import hashlib

def get_password():
    password = ""

    print("Enter Password: ", end="", flush=True)

    while True:
        char = msvcrt.getwch()

        if char == "\r":  # Enter key
            print()
            break

        elif char == "\b":  # Backspace
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        elif char in ("\x00", "\xe0"):  # Special keys
            msvcrt.getwch()

        else:
            password += char
            print("*", end="", flush=True)

    return password


pas = get_password()
hashpas = hashlib.sha256(pas.encode()).hexdigest()

print("Password captured successfully!")
print("Password Hash:", hashpas)