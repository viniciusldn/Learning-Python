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

# Uma dependência é simplesmente um objeto que a sua classe precisa para funcionar. A dependência é
# injetada à classe que a utiliza, ou seja, obrigatoriamente ela precisa ser externa a essa classe.
# Isso quer dizer que, para que haja uma injeção de dependência, a instanciação de um objeto não
# deve se dar dentro da classe, mas do lado de fora dela e então, injetada.
from typing import Type


class Provedora:

    def __init__(self) -> None:
        self.__acao = 'Correr'

    def agir(self) -> str:
        return 'Realizando ação'

    def get_estado(self) -> bool:
        return self.__acao

class Dependente:

    def __init__(self) -> None:
        self.__atributo = 'atributo'

    def iniciar_acao(self, dependencia: any) -> None:
        print(dependencia.agir().lower())

    def identificar_acao(self, dependencia: any) -> None:
        print(dependencia.get_estado())


objeto1 = Provedora()
objeto2 = Dependente()

objeto2.iniciar_acao(objeto1)
objeto2.identificar_acao(objeto1)
print()

# Para aumentar a dependencia, podemos tranformar o parametro de dependencia em um atributo da classe
# dependente, dessa forma a classe dependente encorpora os atributos e metodos da classe provedora.

#Exemplo:

class Dono:

    def __init__(self) -> None:
        self.__comida = 'Ração'
        self.__bebida = 'Água'
        self.__carinho = 'Carinho'

    def get_comida(self):
        return self.__comida

    def get_bebida(self):
        return self.__bebida

    def get_carinho(self):
        return self.__carinho


class Pet:

    def __init__(self, nome: str, dependencia: Type[Dono]) -> None:
        self.__nome = nome
        self.__dependencia = dependencia

    def quer_comer(self):
        print('{} está comendo {}' .format(self.__nome, self.__dependencia.get_comida().lower()))

    def quer_beber(self):
        print('{} está bebendo {}' .format(self.__nome, self.__dependencia.get_bebida().lower()))

    def pedir_carinho(self):
        print('{} está pedindo {}'.format(self.__nome, self.__dependencia.get_carinho().lower()))

dependente = Pet('Bob',Dono())

dependente.pedir_carinho()

# No exeplo a cima, a classe Pet é totalmente dependente da classe Dono, este tipo de prática não é
# recomendável, pois se por acaso a clase dono deixar de existir, a classe pet para de funcionar.
# Para que isso nao aconteca devemos aplicar o conceito de inverção de depencencia.