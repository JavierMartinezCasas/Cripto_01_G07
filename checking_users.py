import json
import os


def checking_users(number):
    if os.path.exists('users_data.json'):
        # leer el json y comprobar que esta registrado el numero, de no ser el caso, devuelve error
        with open('users_data.json') as file:
            dat = json.load(file)
        for i in dat['Users']:
            if number == i['Number']:
                print("Coincidence with number found")
                return True

        print("Error: no coincidences found")
        return False

    else:
        print("Error: no hay ningun usuario registrado aun en la base de datos")
        return False
