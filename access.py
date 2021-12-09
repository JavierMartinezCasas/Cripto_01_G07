import json
from checking_users import checking_users
from json_atributos import json_atributos
from cryptography.fernet import Fernet
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
            print("The money in your account is: " + str(i['Money']) + "€")

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
                if certificateTrans(i, receiver, money):
                    key = Fernet.generate_key()
                    f = Fernet(key)
                    money = str(money)
                    money = money.encode()
                    token = f.encrypt(money)
                    receive_money(sender, receiver, token, money, key, f, i)

                else:
                    print('Error')

            else:
                key = Fernet.generate_key()
                f = Fernet(key)
                money = str(money)
                money = money.encode()
                token = f.encrypt(money)
                receive_money(sender, receiver, token, money, key, f, i)

    else:
        print('There is not any user with that phone number, please try again')
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


def certificateTrans(i, reciver, money):
    message = str(random.randrange(100000000, 999999999, 1))
    message = message.encode()
    if str(i['Type']) == 'A':
        with open("B/Bkey.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=b'\x6f\x70\x65\x6e\x73\x73\x6c\x20\x72\x65\x71\x20\x2d\x69\x6e\x20\x41\x72\x65\x71\x2e\x70\x65\x6d\x20\x2d\x74\x65\x78\x74\x20\x2d\x6e\x6f\x6f\x75\x74',
                backend=default_backend()
            )
    else:
        with open("A/Akey.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=b'\x6f\x70\x65\x6e\x73\x73\x6c\x20\x72\x65\x71\x20\x2d\x69\x6e\x20\x41\x72\x65\x71\x2e\x70\x65\x6d\x20\x2d\x74\x65\x78\x74\x20\x2d\x6e\x6f\x6f\x75\x74',
                backend=default_backend()
            )

    public_key = private_key.public_key()

    encrypted = public_key.encrypt(
        message, padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    if usuario_receptor(encrypted, reciver, private_key, public_key):
        return True
    else:
        return False


def usuario_receptor(encrypted, reciver, private_key, public_key):
    de_message = private_key.decrypt(encrypted, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
                                     )
    # firma el mensaje que ha descifrado con la clave privada del certificado.

    signature = private_key.sign(
        de_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print()
    print("Correct validation!")

    if id_user(signature, de_message, public_key) is None:
        return True
    else:
        return False


def id_user(signature, de_message, public_key):
    # el usuario utiliza la clave publica de la entidad que esta en conocimiento de todos para obtener la clave publica

    mar = public_key.verify(signature, de_message,
                            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                        salt_length=padding.PSS.MAX_LENGTH
                                        ),
                            hashes.SHA256()
                            )

    return mar
