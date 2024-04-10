def encode(password):
    encoded_password = ""
    for char in password:
        char = int(char) + 3
        encoded_password = f"{encoded_password}{char}"
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
	decoded_digit = (int(digit) - 3) % 10
	decoded_password += str(decoded_digit)
    return decoded_password

def print_menu():
    print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')

while True:
    print_menu()
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
    elif option == 2:
        print(f"The encoded password is {encode(password)}, and the original password is {decode(encode(password))}")
    elif option == 3:
        break
