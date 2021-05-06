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


# A herança de classes, permite a uma classe herdeira utilizar metodos e atributos
# públicos da classe mãe.
# A herança é aplicada quando utilizamos uma classe como "parametro" para outra

# Exemplo:

class Main:  # Classe mãe

    def __init__(self, dividir) -> None:
        self.main = 'contar'  # Atributo público
        self.__main = 'multiplicar'  # Atributo privado
        self.operacao = dividir

    def contar(self) -> None:  # Método público
        print(self.main)

    def __multiplicar(self) -> None:  # Método privado
        print(self.__main)


class Herdeira(Main):

    def __init__(self) -> None:
        super().__init__('dividir')  # a função super()
        # é usada para acessar metodos e propriedades da classe mãe

    def recontar(self) -> None:
        print(f'Re{self.main}')

    def remultiplicar(self) -> None:
        print(f'Re{self.__main}')

    def __dividir(self) -> None:
        print(self.operacao)

    def dividir(self) -> None:
        print(self.operacao)


herdeira = Herdeira()

herdeira.contar()
herdeira.recontar()
# herdeira.__multiplicar() -> AttributeError: 'Herdeira' object has no attribute '__multiplicar'
# herdeira.remultiplicar() -> AttributeError: 'Herdeira' object has no attribute '_Herdeira__main'
# herdeira.__dividir() -> AttributeError: 'Herdeira' object has no attribute '__dividir'
herdeira.dividir()
