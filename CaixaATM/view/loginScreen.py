from controller.userController import UserController
user = UserController()

class LoginScreen:
    def __init__(self):
        print("------------------------------------------------")
        print("                     LOGIN")
        cpf_cnpj = input("Insira o seu cpf ou CNPJ: ")
        password = input("Insira sua senha: ")
        print("------------------------------------------------")
        loggedUser = user.login(cpf_cnpj,password)

        while True:
            print("\n------------------------------------------------")
            print("         Menu")
            print("1 - Extrato")
            print("2 - Saque")
            print("3 - Depósito")
            print("4 - Solicitar crédito")
            print("5 - Sair")
            print("------------------------------------------------")
            option = input(">> ")

            if option=="1":
                user.consultarExtrato(loggedUser)
            elif option=="2":
                user.sacar(loggedUser)
            elif option=="3":
                user.depositar(loggedUser)
            elif option=="4":
                user.solicitarCredito(loggedUser)
            elif option >"5":
                print("Opção inválida")

            if option=="5":
                break