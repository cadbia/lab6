def encoder(password):
    # Initialize an empty string to store the encoded password
    encoded = ''

    # Loop through each character in the input password
    for char in password:
        # Check if the character is a digit
        if char.isdigit():
            # Convert the digit to an integer, add 3, take modulo 10 to handle overflow, add back to the encoded string
            encoded += str((int(char) + 3) % 10)

    return encoded


def main():
    # Initialize variables to store the encoded and original passwords
    encoded_password = ''
    original_password = ''

    while True:
        # Print the menu options
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = input("Please enter an option: ")

        if option == '1':
            # If the user chooses to encode a password
            original_password = input("Please enter your password to encode: ")
            # Encode
            encoded_password = encoder(original_password)
            print('Your password has been encoded and stored!')
            print()
        elif option == '2':
            # If the user chooses to decode a password
            if encoded_password:
                # If a password has been encoded, display the encoded and original passwords
                print(f'The encoded password is {encoded_password}, and the original password is {original_password}.')
                print()
        elif option == '3':
            break


if __name__ == "__main__":
    main()
