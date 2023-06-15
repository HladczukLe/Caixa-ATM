from controller.managerController import ManagerController
manager = ManagerController()

class RegisterScreen():
    def __init__(self):
        print("------------------------------------------------------")
        print("Faça seu cadastro")
        self.name = input("Digite o seu nome e sobrenome: ")
        self.cpf_cnpj = input("Digite o CPF ou CNPJ: ")
        self.adress = input("Digite o endereço: ")
        self.phone = input("Digite o telefone: ")
        self.password = input("Digite a senha (no mínimo 6 digitos numéricos): ")
        print("------------------------------------------------------")

        manager.registerUser(self.name, self.cpf_cnpj, self.adress, self.phone, self.password)
