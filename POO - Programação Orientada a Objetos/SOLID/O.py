"""Open-Closed Principle"""


# O módulo é considerado fechado se estiver disponível para uso por ouytros mó'dulos
# Isso pressupõe que o módulo recebeu uma descrição bem definida e estável
# é recomendavél que os módulos sejam abertos, isso evita a realteração de um codigo
# um módulo é considerado aberto se for passivel de extensão sem necessidade de alterações

# Codigo de teste (já com aplicação do principio de responsabilidade unica)
class Circo:
    """
    # Observe que o codigo teste está fechado, pois suas possibilidades de execução
    # se limitam ao parametro tipo que tem apenas 2 comportamentos

    def apresentar(self, tipo):# Método que gerencia o processo
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()

    # Para tornar o método gerenciador aberto, ele deve ter n possibilidades de
    # comportamento sem a necessidade que altera-lo para cada nova possibilidade
    """

    # Ao alterar o tipo de apresentador pelo proprio apresentador alteramos a
    # responsabilidade da ação para o proprio apresentador
    # assim o metodo apresentar agora gerencia os apresentadores e estes gerenciam
    # suas ações assim podemos ter infinitos apresentadores

    def apresentar(self, apresentador: any) -> None:
        apresentador.apresenta_show()

    """
    # Desta forma cada apresentador terá sua classe, responsável por suas próprias
    # ações, este é o conseido de Associação de Classes
    
#metodos que executam ações
    def apresentar_malabarista(self):
        print('O malabarista se apresentou')

    def apresentar_palhaco(self):
        print('O palhaço se apresentou')
    
    # Assim para adicionar novos apresentadores basta criar uma classe,
    # sem necessidade de alterar o codigo gerenciador
    """

class Malabarista:

    def apresenta_show(self) -> None:
        print('O malabarista se apresentou')

class Palhaco:

    def apresenta_show(self)-> None:
        print('O Palhaço se apresentou')

class Domador():

    def apresenta_show(self)-> None:
        print('O Domador se apresentou')

# Classes sempre devem ser instanciadas
circo = Circo()  # instanciar a classe
palhaco = Palhaco()
malabarista = Malabarista()
domador = Domador()

circo.apresentar(domador)