def encode(password):
    encoded = ""
    for i in password:
        encoded = encoded + str(int(i)+3)
    return encoded



def decode(password):
    decoded_pass = ''
    for digit in password:
        decoded_pass += str((int(digit) - 3))
    return decoded_pass

def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    print('Please enter an option:', end = " ")


def main():
    go = True
    while go:
        print_menu()
        option = input()
        if option == '1':
            print('Please enter your password to encode:', end=" ")
            password = encode(input())
            print('Your password has been encoded and stored!')
            print()
        if option == '2':
            print(f'The encoded password is {password} and the original password is ')
            print()
        if option == '3':
            go = False


if __name__== '__main__':
    main()