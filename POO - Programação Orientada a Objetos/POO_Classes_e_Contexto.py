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
"""
Classes são abstrações de um elemento com ações(metodos) e caracteristicas(atributos)
Metodos e atributos são respectivamente funções e variáveis de uma instância, ou seja
podem ser acessados através de um objeto instanciado 
"""
#classe de teste
class AbtractionClass:

    def __init__(self, atributo) -> None:  # Metodo contrutor indicam as caracteristicas(atributos) da classe e
        # definem a mesma, sendo os primeiros metodos a serem rodados ao acessar uma classe.
        # o indicador self diz respeito ao objeto instanciado, assim
        self.class_atributo_predefinido = 'Classe utilizada para aprender.'
        """Alguns atributos podem ser definidos posteriormente, para isso eles
        devem ser colocados como parametros no metodo construtor e indicados ao instanciar a classe.
        """
        self.class_atributo_posdefinido = atributo

    def metodo_acao1(self) -> None:  # Metodos tem parametros(indicadores) self faz referencia a classe a qual o
        # metodo esta inserido.
        print('Metodo/Ação concluido')

    def metodo_acao2(self, num: int, mult: int) -> int:  # num e mult são parametros relevantes a ação.
        return num * mult

    def metodo_acao3(self) -> None:  # metodos podem utilizar atrbutos da classe.
        print('{} da {}'.format(self.class_atributo_posdefinido,self.class_atributo_predefinido))

"""
Um objeto deve ser criado como instancia para que uma classe possa ser acessada.
Em seguida os metodos e atributos desejados pedem ser acessados através do objeto.
"""
"""Comandos de teste da classe e dos métodos:
objeto = AbtractionClass('Sou um atributo pós-definido')  # Instanciando Objeto, atributos da classe pós-definidos são
# indicados dentro dos parenteses.

objeto.metodo_acao1()  # acessando metodo atraves da instancia.
print()
print(objeto.metodo_acao2(20, 10))  # metodos podem ser acessados de forma direta.
result = objeto.metodo_acao2(10, 10)  # ou indireta (agrega a resposta da ação a uma variável.
print(result)
print()
print(objeto.class_atributo_predefinido)  # atributos podem ser acessados diretamente, assim como metodos.
atributo = objeto.class_atributo_posdefinido  # ou indiretamente.
print(atributo)
print()
objeto.metodo_acao3()
"""

# Exemplo do passarinho

class Passarinho:

    def __init__(self, especie: str):
        self.passaro = especie

    def voar(self, voo: bool) -> None:
        if voo is True:
            print(f'O {self.passaro} esta voando')
        else:
            print(f'O {self.passaro} esta pousado')

    def gostar(self, gosto: str) -> None:
        print('O {} gosta de {}' .format(self.passaro, gosto))

    def cantar(self, music) -> None:
        print('O {} esta cantando {}' .format(self.passaro, music))
"""
bird1 = Passarinho('papagaio')

bird1.voar(True)
bird1.gostar('musica')
bird1.cantar('feliz')
print()

bird2 = Passarinho('Colibri')

bird2.voar(False)
bird2.gostar('voar')
bird2.cantar('Carmem Miranda')
"""

Passarinho('colibri').cantar('rock')