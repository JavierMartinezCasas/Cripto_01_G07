import json
import os


def login():
    if os.path.exists('users_data.json'):
        print("To log into your account introduce the following data:")
        print()

        number = input("Input your number: ")
        password = input("Input your password: ")

        # leer el json y comprobar que esta registrado el numero, de no ser el caso, devuelve error
        with open('users_data.json') as file:
            dat = json.load(file)

        for i in dat['Users']:
            # print("Number: ", i['Number'])
            if number == i['Number']:
                print("Coincidence with number found")
                if password == i['Password']:
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
