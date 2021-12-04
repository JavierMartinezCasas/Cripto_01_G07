import json
from checking_users import checking_users
from json_atributos import json_atributos
from cryptography.fernet import Fernet


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
        elif money >= 500:
            certificateTrans(money, i)
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


def certificateTrans(money, i):
    return
