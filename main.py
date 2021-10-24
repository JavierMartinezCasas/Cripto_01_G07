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
        if i is not None:
            access(i)
        return
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
            if i is not None:
                access(i)
        elif election == 'N':
            print("To register as a new user, introduce the following data:")
            print()
            register()


boot()
