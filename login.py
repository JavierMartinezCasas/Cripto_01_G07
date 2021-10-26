import json
import os
import hashlib
import hmac


def login():
    if os.path.exists('users_data.json'):
        print("To log into your account introduce the following data:")
        print()

        number = input("Input your number: ")
        password = input("Input your password: ")

        key = str("101")
        password = str(password)

        new_password = hmac.new(key.encode(), password.encode(), hashlib.sha512).hexdigest()

        # leer el json y comprobar que esta registrado el numero, de no ser el caso, devuelve error
        with open('users_data.json') as file:
            dat = json.load(file)

        for i in dat['Users']:
            # print("Number: ", i['Number'])
            if number == i['Number']:
                print("Coincidence with number found")
                if new_password == i['Password']:
                    print("Correct password")
                    print()
                    print("Welcome to your account")
                    return i

                else:
                    print("Error: Incorrect password")
                    return

        print("Error: No coincidences found")
        return

    else:
        print("Error: No user registered yet in the database")
        return None
