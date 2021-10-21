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

def send_money():
    sender= login()
    reciver =input('Please, introduce the phone number where do you please to send the money: ')
    if checking_user(reciver)==1:
        money=input('Introduce the amount of money thet you want to sent:')
    #aqui tendriamos que encriptar el dinero, llamar a la función recivir el dinero donde se desencriptará
    #se comrpobará que corresponde con la cantidad de dinero que ha querido ser envíada desde send_money
    #y se dispondrá a reducir y aumentar el saldo en la cuenta de cada uno.