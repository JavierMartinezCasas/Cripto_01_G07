import json
import os
import hashlib
import hmac
import json_atributos


def login():
    if os.path.exists('users_data.json'):
        print("To log into your account introduce the following data:")
        print()

        number = input("Input your number: ")
        password = input("Input your password: ")

        key = json_atributos.json_atributos(number, 'Key')
        password = str(password)
        new_password = hmac.new(key.encode(), password.encode(), hashlib.sha512).hexdigest()

        with open('users_data.json') as file:
            dat = json.load(file)

        for i in dat['Users']:
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
