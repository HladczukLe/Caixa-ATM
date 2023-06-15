from controller.managerController import ManagerController
manager = ManagerController()

class RemoveScreen():
    def __init__(self):
        print("---------------------------------------------------------------------------------------------")
        print("                     REMOVER USUÁRIO")
        cpf_cnpj = input("Digite o CPF ou CNPJ do cliente a ser removido: ")
        password = input("Insira a senha: ")
        print("---------------------------------------------------------------------------------------------")
        manager.removeUser(cpf_cnpj,password)