#AMIT BABU KHATRI
#np03cs4s230291
def welcome():
    print('Welcome to the Caesar Cipher\n'
          'This program encrypts and decrypts text with the Caesar Cipher.')


def enter_message():
    while True:
        choice = input('Would you like to encrypt (e) or decrypt (d): ')
        choice = choice.lower()
        if choice != 'e' and choice != 'd':
            print('Invalid Mode')
            continue

        if choice == 'e':
            ed = 'encrypt'
        else:
            ed = 'decrypt'
 
        while True:
            message = input('What message would you like to % s: ' % ed)
            if message.replace(" ", "").isalpha():
                message = message.upper()
                break
            else:
                print('Invalid input, please ensure that the message '
                      'contains only letters between A and Z.')

        while True:
            shift = input('What is the shift number: ')
            try:
                shift = int(shift)
                break
            except ValueError:
                print('Invalid Shift')
                continue
        return choice, message, shift


def encrypt(message, shift):
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    encrypted_message = ""
    for char in message:
        if char == ' ':
            encrypted_message += ' '
        else:
            number = alphabet.index(char)
            finaleNumber = (number + shift) % 26
            encrypted_message += alphabet[finaleNumber]

    answer = encrypted_message
    return answer


def decrypt(message, shift):
    shift = - shift
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    decrypted_message = ""
    for char in message:
        if char == ' ':
            decrypted_message += ' '
        else:
            number = alphabet.index(char)
            finaleNumber = (number + shift) % 26
            decrypted_message += alphabet[finaleNumber]

    answer = decrypted_message
    return answer


def main():
    welcome()
    while True:
        choice, message, shift = enter_message()
        if choice.lower() == 'e':
            answer = encrypt(message, shift)
        else:
            answer = decrypt(message, shift)
        print(answer)
        again = input('Would you like to encrypt or decrypt '
                      'another message? (y/n): ')
        if again.lower() == 'n':
            print('Thanks for using the program, goodbye!')
            break


main()
