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


# VariÁveis estáticas ou variÁveis de classe são variaveis internas de uma classe, é recomendável que este tipo de
# variável seja substituido por um atributo de classe

class ClasseTeste:
    estatico = 'Variável Estática'

    def __init__(self, estado: bool) -> None:
        self.estado = estado
        self.atributo = 'Atributo'


object1 = ClasseTeste(True)
object2 = ClasseTeste(False)
object3 = ClasseTeste(True)

# Variáveis estaticas podem ser acessadas utilizando a propria classe como instância ou através do objeto onde a
# classe foi instanciada. Ela pode ainda, ser alterada de forma independente a cada instância, ou alterada para todas
# as instancias de uma classe.
# Alterações nas instancias sobrepoe as alterações feitas pela classe, pois seu peso é modular

print('\nClassse teste 1\n')
object2.estatico = 'Variável de Classe'  # alterar a variável apenas para instância object2.
object1.estatico = 'Variável Estática'
ClasseTeste.estatico = 'Variável alterada pela classe'  # alterar variável diretamente classe e para todos seus
# metodos e instâncias)


print(ClasseTeste.estatico)
print(object1.estatico)
print(object2.estatico)
print(object3.estatico)


class ClasseTeste2:
    classvar = 'Variável de Classe'

    def __init__(self) -> None:
        self.atributo = 'teste de variáveis estáticas'

    def imprimir_estatico(self) -> None:
        print(self.classvar)  # A instancia precisa ser declarada para imprimir uma classe estática pelo metodo

    def alterar_estatico(self, novo: any) -> None:
        self.classvar = novo


print('\nClassse teste 2\n')
objeto1 = ClasseTeste2()

objeto1.alterar_estatico('Variável estática')
objeto1.imprimir_estatico()
ClasseTeste2().imprimir_estatico()

print('\nExemplo Prático\n')


class Entregador:
    """
    Esta equipe de entregas, tem um salario fixo acrescido de um bonus relativo ao número total de entregas mensais.
    """
    entregas_mes = 0

    def __init__(self, nome: str, entreguas: int) -> None:
        self.nome = nome
        self.entreguas = entreguas

    def ver_rendimento(self) -> None:
        print(f'Nome: {self.nome}\n'
              f'Entregas: {self.entreguas}\n')

    def ver_comissao(self) -> None:
        print(f'Bonus mensal: {Entregador.__calcular_comissao()}\n')

    @classmethod  # Decorator é um método para envolver uma função, modificando seu comportamento, dessa forma a ação
    # seguinte ao decorador fica encapsulada, podemos trambem criar decoradores através de funções pré estabelecidas,
    # Eles são muito utilizados para trabalhar com metaprogramação de um modo rápido de em Python
    def __calcular_comissao(cls) -> float:
        return cls.entregas_mes * 4.5

    @classmethod
    def entregas_mensais(cls, total_entregas: int) -> float:
        cls.total_entregas = total_entregas
        cls.__calcular_comissao()


entregador1 = Entregador('Roberto', 7)
entregador2 = Entregador('Eliane', 33)

entregador1.ver_rendimento()
entregador2.ver_rendimento()

entregador2.entregas_mensais(40)

entregador1.ver_comissao()
entregador2.ver_comissao()

# No exemplo abaixo temos uma classe como todos os tipos de classes e metodos apresentados

class ClasseExemplo:
    varivel_de_classe = 'Váriavel Estática'

    def __init__(self, publico: str, privado: bool) -> None:
        self.atributo1 = publico
        self.__atributo2 = privado

    def metodo_publico(self) -> None:
        print('Método público')

    def __metodo_privado(self) -> int:
        print('Método Privado')
        return 1

    @staticmethod  # Decorator
    def metodo_estatico() -> None:
        print('Método Estático')