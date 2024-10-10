while True:
        plen_input = input("Enter password length\n")
        
        # Check if the input contains only digits
        if not plen_input.isdigit():
            print("Invalid input! Please enter a valid positive number.")
            continue

        # Convert input to an integer
        plen = int(plen_input)

        # Check if the input length is within a valid range
        if plen <= 0:
            print("Password length must be greater than 0. Please try again.")
        # elif plen > # max_length:
        #     print(f"Password length too long! Maximum is {#max_length}. Please try again.")
        # else:
        #     break