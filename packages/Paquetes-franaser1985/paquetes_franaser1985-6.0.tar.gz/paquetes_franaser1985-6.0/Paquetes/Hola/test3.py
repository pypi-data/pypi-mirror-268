#Paquetes nos ayudan a tener varios modulos en un solo archivo y hasta submodulos, y permiten distribuirse 

import numpy as np

def saludar():
    print("Hola, te saludo desde saludos.saludar()")

def prueba():
    print("Esto es una nueva prueba de la nueva version 6.0")

def generar_arrray(numeros):
    return np.arange(numeros)

#print(__name__)
class Saludo():

    def __init__(self):
        print("Hola, te saludo desde Saludo.__init__()")
# Para cuando se llame desde otro fichero no se ejecute dos veces la función osea evita que se ejecute el codigo con las pruebas
# __name__ alamcena durante la ejecución de un programa el nombre del script
if __name__ == '__main__':
    #saludar()
    print(generar_arrray(5))