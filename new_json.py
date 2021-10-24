import json
import os
import json_atributos


def new_json(number,money):
    nombre= 'First_name'
    name=json_atributos.json_atributos(number,nombre)
    apellido='Last_name'
    last_name=json_atributos.json_atributos(number, apellido)
    contraseña='Password'
    password=json_atributos.json_atributos(number, contraseña)
    if os.path.exists('users_data.json'):
        #leer el json y comprobar que esta registrado el numero, de no ser el caso, devuelve error
        with open('users_data.json') as file:
            dat = json.load(file)

        for i in dat['Users']:
            if number == i['Number']:
                dup i[nombre]
                #delete


        print("Error: no coincidences found")
        return

    else:
        print("Error: no hay ningun usuario registrado aun en la base de datos")
        return





