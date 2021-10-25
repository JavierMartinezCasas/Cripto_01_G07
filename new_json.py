from pathlib import Path
import json
import os


def new_json(sender, receiver, sender_money, receiver_money):
    if os.path.exists('users_data.json'):
        with open('users_data.json') as file:
            dat = json.load(file)
            auxiliar = []
            for i in dat['Users']:
                if i['Number'] == sender:
                    i['Money'] == sender_money
                if i['Number'] == receiver:
                    i['Money'] == receiver_money
                auxiliar.append(i)
    actualizarJson(auxiliar)
    return


def actualizarJson(auxiliar):  # pasamos la lista que contiene los diccionarios para actualizar el JSON
    with open('users_data.json') as file:
        dat = json.load(file)

    try:
        with open('users_data.json', 'w') as f:
            json.dump(auxiliar, f, indent=1)
    except FileNotFoundError as ex:
        raise Exception("lectura erronea del json") from ex
