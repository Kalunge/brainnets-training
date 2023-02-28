# The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
# encrypts letters by shifting them over by a 
# certain number of places in the alphabet. We 
# call the length of shift the key. For example, if the 
# key is 3, then A becomes D, B becomes E, C becomes 
# F, and so on. To decrypt the message, you must shift 
# the encrypted letters in the opposite direction. This 
# program lets the user encrypt and decrypt messages 
# according to this algorithm.

# When you run the code, the output will look like this:

# Do you want to (e)ncrypt or (d)ecrypt?
# > e
# Please enter the key (0 to 25) to use.
# > 4
# Enter the message to encrypt.
# > Meet me by the rose bushes tonight.
# QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


# Do you want to (e)ncrypt or (d)ecrypt?
# > d
# Please enter the key (0 to 26) to use.
# > 4
# Enter the message to decrypt.
# > QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# MEET ME BY THE ROSE BUSHES TONIGHT.

def ceaser_cipher():
    # The string of letters in the alphabet. We'll use this to find the index of 
    # each letter in the alphabet.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Ask the user if they want to encrypt or decrypt a message.
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    choice = input("> ")

    # Ask the user for the key to use.
    print("Please enter the key (0 to 25) to use.")
    key = int(input("> "))

    # Ask the user for the message to encrypt or decrypt.
    print("Enter the message to encrypt.")
    message = input("> ")

    # Make the message all uppercase letters.
    message = message.upper()

    # This string will hold the encrypted or decrypted message.
    new_message = ""

    # Loop through each character in the message.
    for character in message:
        # If the character is in the alphabet, encrypt or decrypt it.
        if character in alphabet:
            # Get the encrypted or decrypted number for this character.
            position = alphabet.find(character)
            if choice == "e":
                new_position = (position + key) % 26
            elif choice == "d":
                new_position = (position - key) % 26

            # Add the encrypted or decrypted number's letter to our new message.
            new_message += alphabet[new_position]
        else:
            # Just add the character without encrypting or decrypting.
            new_message += character

    # Tell the user the encrypted or decrypted message.
    print(new_message)



ceaser_cipher()