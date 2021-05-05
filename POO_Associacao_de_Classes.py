# language: PT
"""
Existem alguns padrões de bas práticas na programação.

É aconselhavél que:
    - Classes sejam nomeadas com substantivos e a primeira letra capital.
    - Atributos de classe sejam nomeados com substantivos minusculos.
    - metodos sejam nomeados com verbos que indiquem sua ação.
    - Utilizar typing notations, indicando caracteristicas de funções e metodos.
    - indicar a linguagem na qual esta programando no começo do codigo.
"""
from time import asctime
from typing import Type

class Motores:

    def __init__(self, numero_de_serie: any) -> None:
        self.__atributo1 = numero_de_serie

    def ligar(self) -> None:
        print(f'Inicializando motor {self.__atributo1}')

    def desligar(self) -> None:
        print(f'Desligando motor {self.__atributo1}')


class Operador:

    def __init__(self, nome: str, turno: str):
        self.nome = nome
        self.turno = turno

    def ligar_motor(self, motor: Type[Motores]):
        print(asctime())
        motor.ligar()

    def desligar_motor(self, motor: Type[Motores]):
        print(asctime())
        motor.desligar()

    def intervalo(self):
        print(asctime())
        print('Hora de comer')

operador1 = Operador('Carlos', 'Tarde')
motor1 = Motores('M01')
motor2 = Motores('M02')
motor3 = Motores('M03')

#motor1.ligar()
operador1.ligar_motor(motor1)
operador1.intervalo()