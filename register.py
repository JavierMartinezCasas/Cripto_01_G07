"""En este archivo se comprueban los datos de registro, es decir, si hay un usuario intentando registrar el mismo
numero de telefono varias veces. Ademas se crea la base de datos y se añaden nuevos usuarios a la misma"""

import json
import os
import hashlib
import hmac
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def users_data():
    name = input("Input your name: ")
    last_name = input("Input your last name: ")
    password = input("Input your password: ")
    number = input("Input your phone number: ")
    money = input("Input the max amount amount of money you want to use in our app: ")

    key = str(random.random())
    password = str(password)
    hmac_password = hmac.new(key.encode(), password.encode(), hashlib.sha512).hexdigest()

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    dat = {'Users': []}

    dat['Users'].append({
        'First_name': name,
        'Last_name': last_name,
        'Password': hmac_password,
        'Number': number,
        'Money': money,
        'Key': key,
        'Public key': public_key,
        'Private key': private_key
    })

    return dat


def passCheck(password):
    password = str(password)
    min_length = False
    mayus = False
    num = False
    sign = False

    mayus_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                  "T", "U", "V", "W", "X", "Y", "Z"]

    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    sign_list = ["º", "@", "#", "!", "$", "%", "&", "ç", "¿", "?", "¡", "-", "_", ".", ":", ";", ",", "*", "+", "~"]

    for i in password:
        if len(password) >= 8:
            min_length = True
        if i in mayus_list:
            mayus = True
        if i in num_list:
            num = True
        if i in sign_list:
            sign = True

    if min_length is True and mayus is True and num is True and sign is True:
        return True

    else:
        return False


def register():
    """Comprueba que los datos introducidos son validos y añade al usuario a la base de datos (users_data.json)"""
    if os.path.exists('users_data.json'):
        name = input("Input your name: ")
        last_name = input("Input your last name: ")

        print()
        print("The password needs to be at least 8 characters long and must include at least 1 number, 1 capital "
              "letter and 1 sign (@,#,~, etc...)")
        password = input("Input your password: ")
        while not passCheck(password):
            print()
            print("Error: Incorrect password, try again following the instructions above")
            password = input("Input your password: ")
        print("Password validated, continue your registration")
        print()

        """if passCheck(password):
            print("Password validated, continue your registration")
            print()
        else:
            print("Error: Incorrect password, try following the instructions above")
            return"""
        number = input("Input your phone number: ")
        money = input("Input the max amount amount of money you want to use in our app: ")

        key = str(random.random())
        password = str(password)
        hmac_password = hmac.new(key.encode(), password.encode(), hashlib.sha512).hexdigest()

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

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
                'Money': money,
                'Key': key,
                'Public key': public_key,
                'Private key': private_key
            })

            with open('users_data.json', 'w') as f:
                json.dump(dats, f, indent=1)

    else:
        with open('users_data.json', 'w') as file:
            json.dump(users_data(), file, indent=1)
