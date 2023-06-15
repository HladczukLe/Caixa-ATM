from controller.managerController import ManagerController
manager = ManagerController()

class ViewUserScreen():
    def __init__(self):
        print("---------------------------------------------------------------------------------------------")
        print("                     VER USUÁRIO")
        cpf_cnpj = input("Digite o CPF ou CNPJ do cliente que você deseja ver: ")
        password = input("Insira a senha: ")
        print("---------------------------------------------------------------------------------------------")

        manager.viewUser(cpf_cnpj,password)