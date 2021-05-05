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

# Métodos estáticos, são utilizados como especificadores dentro de uma classe e não recebem um argumento inicial

class MetodosEstaticos:

    def __init__(self, estado: str) -> None:
        self.estado = estado

    @staticmethod  # Decorador similar ao @classmethod, porém transforma a função em um método estático
    def metodo_estatico() -> None:
        print('Não recebo argumentos e não acesso outras informações da classe')


MetodosEstaticos.metodo_estatico()