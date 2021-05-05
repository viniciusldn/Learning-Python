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

"""Single Responsability Principle"""


# Importante se ater as estruturas e passos do projeto para criar modulalos de forma coesa.

# Código de teste (código sem aplicação SRP está entre """ """").
class TrataUnhas:
    """
    def pintar(self, cor: str, limpa: bool) -> None:
        if isinstance(cor, str) and isinstance(limpa, bool):
            if limpa is True:
                print('Unha pintada de {}'.format(cor))
            else:
                print('Unha esta ainda nao foi limpa para ser pintada')
        else:
            print('dados incorretos')
    """

# No código sem SRP, um unico metodo está responsável por diversas ações isso deixa o codigo confuso.
# Ao aplicar princípio SRP para modular o codigo faz com que ele se torne mais claro e suas ações tornam-se
# independentes, facilitanto alterações futuras.

    def pintar(self, cor: str, limpa: bool) -> None:
        if self.__verificarDados(cor, limpa):
            self.__verificarUnhaPintada(cor, limpa)
        else:
            self.__indicarErro()

    def __verificarDados(self, cor: str, limpa: bool) -> bool:
        if isinstance(cor, str) and isinstance(limpa, bool):  # Verifica se os dados inseridos correspondem as
            # instancias desejadas.
            return True
        else:
            return False

    def __verificarUnhaPintada(self, cor: str, limpa: bool) -> None:
        if limpa is True:
            print('Unha pintada de {}.'.format(cor))
        else:
            print('Unha esta ainda nao foi limpa para ser pintada.')

    def __indicarErro(self) -> None:
        print('Dados incorretos sua louca.')
