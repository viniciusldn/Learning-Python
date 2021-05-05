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


# Getters e Setter servem para tratar atributos de uma classe como estados


class Maquina:

    def __init__(self, atributo: bool) -> None:
        self.__estado = atributo  # ligado: True, Desligado: False

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):  # verifica se a entrada é uma instancia boolean
            self.__estado = valor


"""
Tente rodar este codigo direto pelo terminal.
Para isso va para o diretorio do codigo e indique o compilador (python3)
Após a inicialização, três setas  ">>>" indicarão que o terminal do python esta rodando
Agora é só importar a classe, instanciar um objeto e testar os metodos
"""