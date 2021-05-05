#language: PT
"""
Existem alguns padrões de bas práticas na programação.
É aconselhavél que:
    - Classes sejam nomeadas com substantivos e a primeira letra capital.
    - Atributos de classe sejam nomeados com substantivos minusculos.
    - metodos sejam nomeados com verbos que indiquem sua ação.
    - Utilizar typing notations, indicando caracteristicas de funções e metodos.
    - indicar a linguagem na qual esta programando no começo do codigo.
"""
"""
Encapsulamento esta relacionado a permissões de uso
"""


class Estudante:

    def __init__(self, nome: str, idade: int, registro: int) -> None:
        self.nome = nome
        self.idade = idade
        self.registro = registro


estudante1 = Estudante('Vinicius', 30, 1234)

print(f'nome: {estudante1.nome}'
      f'\nidade: {estudante1.idade}'
      f'\nRegistro: {estudante1.registro}'
      f'\n')


# no exemplo a cima todos os atributos de classe podem ser acessados, no entanto no caso de existir um atributo que
# não deve ser acessado basta utilizar __(dois underlines antes do nome do atributo.

class Forum:

    def __init__(self, nome: str, idade: int, email: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__email = email


usuario1 = Forum('Nubia', 32, '1234@test.com')

print(f'Nome: {usuario1.nome}'
      f'\nIdade: {usuario1.idade}'
      #      f'\nEmail: {usuario1.email}'
      # AttributeError: 'Forum' object has no attribute 'email'
      f'\n')


# Entretanto, caso um método seja criado dentro da classe para acessar o atributo privado
# este poderá ser utilizado para retornar o atributo.

class Pagamento:

    def __init__(self, nome: str, numero_cartao: int, vencimento: str) -> None:
        self.nome = nome
        self.__nc = numero_cartao
        self.vencimento = vencimento

    def print_nc(self) -> int:
        return self.__nc


cliente1 = Pagamento('Alberto', 1234456778901470, '10/1010')

print(f'Nome: {cliente1.nome}'
      f'\nNº cartão: {cliente1.print_nc()}'
      f'\nVencimento: {cliente1.vencimento}'
      f'\n')


# Assim como atributos, métodos também podem ser incapsulados, afim por exemplo de protejer uma ação quu faça uso de
# um atributo previamente protegido.

class CompraBebida:

    def __init__(self, idade: int, documento=['nome', 'idd']) -> None:
        self.idade = idade
        self.__documento = documento  # Atributo Privado
        print(f'{self.idade} anos? Parece mais jovem')

    def perguntar_idade(self) -> None:
        if self.idade >= 18:
            print('Verificando documento')
            print(self.__verificar_documento())
        else:
            print('Muito novo para comprar bebidas.')

    def __verificar_documento(self) -> str:  # Método privado.
        print(f'\nNome: {self.__documento[0]}'
              f'\nIdade: {self.__documento[1]} anos\n')
        if self.__documento[1] < 18:
            return 'É ilegal vender para menores de 18 anos.'
        else:
            return 'Obrigado, aqui esta sua bebida.'


beber = CompraBebida(19, ['Renata', 15])
beber.perguntar_idade()
# beber.__verificar_documento() -> AttributeError: 'ComparBebida' object has no attribute '__verificar_documento'
