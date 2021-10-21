"""Programa para la inicialización de los procesos en la aplicación"""
from creacion_json import create_json


def starting():
    election = input('Do you have already an account?(Y/N): ')

    if election == 'Y':
        return
    elif election == 'N':
        create_json()

    while election != 'Y' and election != 'N':
        print('Error: You need to introduce a valid value(Y/N)')
        election = input('Do you have already an account?(Y/N): ')


starting()
