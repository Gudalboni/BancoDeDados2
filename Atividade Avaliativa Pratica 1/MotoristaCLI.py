from Passageiro import Passageiro
from Corrida import Corrida
from Motorista import Motorista

class MotoristaCLI:

    def __init__(motoristaDB, self):
        self.motoristaDB = motoristaDB

    def Menu(self):
        while True:
            print("\nSelecione uma opcao:")
            print("1 - Cadastrar motorista")
            print("2 - Buscar motorista")
            print("3 - Editar motorista")
            print("4 - Excluir motorista")
            print("5 -  Encerrar programa")

            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                self.cadastrarMotorista()

            elif opcao == "2":
                self.buscarMotorista()

            elif opcao == "3":
                self.editarMotorista()

            elif opcao == "4":
                self.excluirMotorista()

            elif opcao == "5":
                break

            else:
                print("Opção inválida.")

    def cadastrarMotorista(self):
        notaMotorista = int(input("Nota do motorista: "))
        nomePassageiro = input("Nome do passageiro: ")
        documentoPassageiro = input("Documento do passageiro: ")
        notaCorrida = int(input("Nota da corrida: "))
        distancia = float(input("Distância percorrida: "))
        valor = float(input("Valor da corrida: "))

        passageiro = Passageiro(nomePassageiro, documentoPassageiro)
        corrida = Corrida(notaCorrida, distancia, valor, passageiro)
        motorista = Motorista([corrida], notaMotorista)

        self.motoristaDB.cadastrar_motorista(motorista)

    def buscarMotorista(self):
        id_motorista = input("ID do motorista: ")
        motorista = self.motoristaDB.buscar_motorista(id_motorista)

        if motorista:
            print("Nota do motorista:", motorista.avaliacao)
            print("Corridas realizadas:")
            
            for corrida in motorista.corridas:
                print(f"Nota da corrida: {corrida.nota}")
                print(f"Distância: {corrida.distancia} km")
                print(f"Preço: R${corrida.valor}")
                print(f"Nome do passageiro: {corrida.passageiro.nome}")
                print(f"Documento do passageiro: {corrida.passageiro.documento}")

    def editarMotorista(self):
        idMotorista = input("Novo ID do motorista: ")
        novaAvaliacao = int(input("Nota: "))
        novoPassageiro = input("Nome do passageiro: ")
        documentoPassageiro = input("Documento do passageiro: ")
        notaCorrida = int(input("Nota da corrida: "))
        Distancia = float(input("Distância: "))
        valor = float(input("Valor: "))

        novoPassageiro = Passageiro(novoPassageiro, documentoPassageiro)
        novaCorrida = Corrida(notaCorrida, Distancia, valor, novoPassageiro)
        novoMotorista = Motorista([novaCorrida], novaAvaliacao)

        self.motoristaDB.atualizar_motorista(idMotorista, novoMotorista)

    def excluirMotorista(self):
        id_motorista = input("ID do motorista a para remoção: ")
        self.motoristaDB.remover_motorista(id_motorista)