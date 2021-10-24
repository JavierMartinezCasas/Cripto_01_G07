import json
import os

#hwdjk
def json_atributos(user,atributo):
    if os.path.exists('users_data.json'):
        number=user
        #leer el json y comprobar que esta registrado el numero, de no ser el caso, devuelve error
        with open('users_data.json') as file:
            dat = json.load(file)

        for i in dat['Users']:
            #print("Number: ", i['Number'])
            if number == i['Number']:
                valor= i[atributo]
                return valor

        print("There's not user with this phone number")
        return

    else:
        print("Error: no hay ningun usuario registrado aun en la base de datos")
        return