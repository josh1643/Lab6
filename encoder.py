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

