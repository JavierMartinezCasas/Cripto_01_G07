import json
from checking_users import checking_users
from json_atributos import json_atributos
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import random

def access(i):
    sel = None
    while sel != '9':
        sel = input("Enter 0 to do a money transfer, enter 1 to check your balance or enter 9 to quit: ")

        if sel == '1':
            print()
            print("The money in your account is: " + i['Money'] + "€")

        if sel == '0':
            send_money(i)
    print("Thank you for using Bizum!")
    quit()


def send_money(i):
    sender = i['Number']
    print()
    receiver = input('Introduce the phone number of the receiving account: ')

    if checking_users(receiver):
        print()
        money = input('Introduce the amount of money that you want to send: ')
        while money == 0:
            money = input('Introduce the amount of money that you want to send: ')

        money = int(money)
        if money > int(i['Money']):
            print('You do not have enough money to perform this transfer')
            access(i)

        else:
            if money >= 500:
                if certificateTrans(money, i, receiver) is True:
                    key = Fernet.generate_key()
                    f = Fernet(key)
                    money = str(money)
                    money = money.encode()
                    token = f.encrypt(money)
                    receive_money(sender, receiver, token, money, key, f, i)

                else:
                    return

            else:
                key = Fernet.generate_key()
                f = Fernet(key)
                money = str(money)
                money = money.encode()
                token = f.encrypt(money)
                receive_money(sender, receiver, token, money, key, f, i)

    else:
        print('There is not any user with that phone number, please, try again')
        access(i)
        return


def receive_money(sender, receiver, token, money, key, f, i):
    des_token = f.decrypt(token)

    if des_token == money:
        print()
        print('The transfer has been done successfully!')
        print()
        account_update(sender, receiver, money, i)

    else:
        print()
        print('Error decrypting money')
        print()
        access(i)
        return


def account_update(sender, receiver, money, i):
    balance_sender = int(json_atributos(sender, "Money"))
    balance_receiver = int(json_atributos(receiver, "Money"))
    balance_sender -= int(money)
    balance_receiver += int(money)

    list_aux = []

    with open('users_data.json') as file:
        dat = json.load(file)

    for j in dat["Users"]:
        if j['Number'] == sender:
            j['Money'] = balance_sender
        if j['Number'] == receiver:
            j['Money'] = balance_receiver
        list_aux.append(j)

    dictionary = {'Users': list_aux}

    with open('users_data.json', 'w') as f:
        json.dump(dictionary, f, indent=1)

    access(i)
    return


def certificateTrans(i, reciver):

    message = random.randrange(100000000, 999999999, 1)
    public_key = json_atributos(i,'Public key')
    encrypted = public_key.encrypt(
        message,padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    usuario_receptor(encrypted,reciver)



def usuario_receptor(encrypted,reciver):

    private_key= json_atributos(reciver,'Private key')

    de_message = private_key.decrypt(encrypted, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
                                     )

    #firma el mensaje que ha descifrado con la clave privada del certificado.

    with open("A/Akey.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    signature = private_key.sign(
        de_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


    id_user(signature,de_message)

    return

def id_user(signature,de_message):

    #el usuario utiliza la clave publica de la entidad que esta en conocimiento de todos para obtener la clave publica

    with open("A/Acert.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    mar=public_key.verify(signature,de_message,
                      padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH)
                      , hashes.SHA256
                      )
    print(mar)
    return mar