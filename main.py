import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
   
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    
    max_length = len(s)
    
    while True:
        try:
            plen = int(input("Enter password length\n"))

            # Check if the input length is within a valid range
            if plen <= 0:
                print("Password length must be greater than 0. Please try again.")
            elif plen > max_length:
                print(f"Password length too long! Maximum is {max_length}. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
   
    random.shuffle(s)
    print("Your password is: ")
    # If you want to join the characters without any separator (like a space or comma), you pass an empty string "".
    print("".join(s[0:plen])) 