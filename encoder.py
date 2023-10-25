def encode(password):
    encoded = ""
    for i in password:
        encoded = encoded + str(int(i)+3)
    return encoded



