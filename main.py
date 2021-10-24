"""Programa para la inicialización de los procesos en la aplicación"""
from register import register
from login import login
from access import access


def boot():
    print("Welcome to Bizum")
    print()
    election = input('Do you have already an account?(Y/N): ')

    if election == 'Y':
        """Se ejecuta la funcion login() del archivo login.py y se accede a la cuenta"""
        i = login()
        access(i)
    elif election == 'N':
        """"Se ejecuta la funcion register() del arhchivo register.py y se accede a la cuenta"""
        print("To register as a new user, introduce the following data:")
        print()
        register()

    while election != 'Y' and election != 'N':
        print('Error: You need to introduce a valid value(Y/N)')
        election = input('Do you have already an account?(Y/N): ')

        if election == 'Y':
            i = login()
            access(i)
        elif election == 'N':
            print("To register as a new user, introduce the following data:")
            print()
            register()


boot()

def send_money(i):
    sender=i['Number']
    reciver =input('Please, introduce the phone number where do you please to send the money: ')
    if checking_user(reciver)==True:
        money=None
        while money == 0:
            money = input('Introduce the amount of money that you want to send: '
        if money > i['Money']:
            print('You do not have enough money to perform this transfer')
            access(i)
        else:
            #función encriptar
            recibir_dinero(reciver, crip_money, money, sender)
    else:
        print('There is not any user with that phone number, please, try again')
        access(i)


def recibir_dinero(reciver,crip_money,money,sender):
    #desencriptamos crip_money
    if decrip_money == money:
        print('The transfer has been done successfully')
        account_update(reciver,sender,money)
    else:
        print('Error decripting money')
        access(i)

def account_update(reciver,sender,money):
