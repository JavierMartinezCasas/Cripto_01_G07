"""En este archivo se crea el Json users_data, que contiene la información de todos los usuarios registrados"""
import json
import os

#hwdjk
def users_data():
    name = input("Input your name: ")
    last_name = input("Input your last name: ")
    password = input("Input your password: ")
    number = input("Input your phone number: ")
    money = input("Input the max amount amount of money you want to use in our app: ")

    dat = {'Users': []}

    dat['Users'].append({
        'First_name': name,
        'Last_name': last_name,
        'Password': password,
        'Number': number,
        'Money': money
    })

    return dat


def create_json():
    if os.path.exists('users_data.json'):
        name = input("Input your name: ")
        last_name = input("Input your last name: ")
        password = input("Input your password: ")
        number = input("Input your phone number: ")
        money = input("Input the max amount amount of money you want to use in our app: ")

        dats = json.load(open('users_data.json'))

        dats['Users'].append({
            'First_name': name,
            'Last_name': last_name,
            'Password': password,
            'Number': number,
            'Money': money
        })

        with open('users_data.json', 'w') as file:
            json.dump(dats, file, indent=1)

    else:
        with open('users_data.json', 'w') as file:
            json.dump(users_data(), file, indent=1)
