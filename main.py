"""Programa para la inicialización de los procesos en la aplicación"""
from register import register
from login import login


def boot():
    election = input('Do you have already an account?(Y/N): ')

    if election == 'Y':
        # Pasa a ejecutarse el login
        login()
    elif election == 'N':
        """"Se ejecuta la funcion register() del arhchivo register.py"""
        print("To register as a new user, introduce the following data:")
        print()
        register()

    while election != 'Y' and election != 'N':
        print('Error: You need to introduce a valid value(Y/N)')
        election = input('Do you have already an account?(Y/N): ')

        if election == 'Y':
            # Pasa a ejecutarse el login
            login()
        elif election == 'N':
            """"Se ejecuta la funcion register() del arhchivo register.py y se accede a la cuenta(por terminar el acceso a la cuenta)"""
            print("To register as a new user, introduce the following data:")
            print()
            register()


boot()

