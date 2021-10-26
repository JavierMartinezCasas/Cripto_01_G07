"""En este archivo se comprueban los datos de registro, es decir, si hay un usuario intentando registrar el mismo
numero de telefono varias veces. Ademas se crea la base de datos y se añaden nuevos  usuarios a la mismc """

import json
import os
import hashlib
import hmac


def users_data():
    name = input("Input your name: ")
    last_name = input("Input your last name: ")
    password = input("Input your password: ")
    number = input("Input your phone number: ")
    money = input("Input the max amount amount of money you want to use in our app: ")


    key = str("101")
    password = str(password)
    hmac_password = hmac.new(key.encode(), password.encode(), hashlib.sha512).hexdigest()
    print(hmac_password)

    dat = {'Users': []}

    dat['Users'].append({
        'First_name': name,
        'Last_name': last_name,
        'Password': hmac_password,
        'Number': number,
        'Money': money
    })

    return dat


def register():
    """Comprueba que los datos introducidos son validos y añade al usuario a la base de datos (users_data.json)"""
    if os.path.exists('users_data.json'):
        name = input("Input your name: ")
        last_name = input("Input your last name: ")
        password = input("Input your password: ")
        number = input("Input your phone number: ")
        money = input("Input the max amount amount of money you want to use in our app: ")

        key = str("101")
        password = str(password)
        hmac_password = hmac.new(key.encode(), password.encode(), hashlib.sha512).hexdigest()
        print(hmac_password)

        with open('users_data.json') as file:
            diction = json.load(file)
            for i in diction['Users']:
                print()
                if number == i['Number']:
                    """Comprueba si el numero de telefono introducido ya esta en la base de datos"""
                    print("Error: your number is already registered in the database")
                    return
            """Añade los datos del nuevo usuario a la base de datos"""
            dats = json.load(open('users_data.json'))

            dats['Users'].append({
                'First_name': name,
                'Last_name': last_name,
                'Password': hmac_password,
                'Number': number,
                'Money': money
            })

            with open('users_data.json', 'w') as f:
                json.dump(dats, f, indent=1)

    else:
        with open('users_data.json', 'w') as file:
            json.dump(users_data(), file, indent=1)
