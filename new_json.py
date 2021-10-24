import json
import os

def new_json(sender,receiver,sender_money,receiver_money):
    if os.path.exists('users_data.json'):
        with open('users_data.json') as file:
            dat = json.load(file)
            auxiliar =()
            for i in dat['Users']:
                auxiliar.append(i)
                print(auxiliar)
                for i in auxiliar:
                    if i['Number'] == sender:
                        i['Money']==sender_money
                        actualizarJson(auxiliar)

                    if i['Number'] == receiver:
                         i['Money'] == receiver_money
                         actualizarJson(auxiliar)


def actualizarJson(auxiliar):  #pasamos la lista que contiene los diccionarios para actualizar el JSON
    dir_home = str(Path.home())
    my_file = dir_home + "\PycharmProjects\CRIPTOGRAFIA_GRUPO16\src\main\cuentas.json"
    try:
        with open(my_file, "w", encoding="utf-8", newline="") as archivo:
            json.dump(auxiliar, archivo, indent=2)
    except FileNotFoundError as ex:
        raise Exception("lectura erronea del json") from ex