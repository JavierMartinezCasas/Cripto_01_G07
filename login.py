import json
import os


def login():
    if os.path.exists('users_data.json'):
        print("To log into your account introduce the following data:")
        print()

        number = input("Input your number: ")
        password = input("Input your password: ")

        #leer el json y comprobar que esta registrado el numero, de no ser el caso, devuelve error
        with open('users_data.json') as file:
            dat = json.load(file)

        for i in dat['Users']:
            print("Number: ", i['Number'])
            if number == i['Number']:
                print("Coincidence with number found")
                if password == i['Password']:
                    print("Correct password")
                    print("Welcome to your account")
                    #Aqui se llamaria a la funcion de acceso a la cuenta
                    return

                else:
                    print("Error: Incorrect password")
                    return

        print("Error: no coincidences found")
        return

    else:
        print("Error: no hay ningun usuario registrado aun en la base de datos")
        return

