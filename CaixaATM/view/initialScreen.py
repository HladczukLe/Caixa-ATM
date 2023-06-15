from view.loginScreen import LoginScreen
from view.registerScreen import RegisterScreen
from view.removeScreen import RemoveScreen
from view.viewUserScreen import ViewUserScreen
from controller.userController import UserController
from controller.managerController import ManagerController


user = UserController()
manager = ManagerController()


class InitialScreen:
    def __init__(self):
        print("---------------------------")
        print("Menu: ")
        print("Escolha um usuário: ")
        print("1 - Cliente ")
        print("2 - Gerente ")
        print("---------------------------")
        option = input(">> ")
        if option=="1":
            LoginScreen()
        elif option=="2":
            print("---------------------------")
            user = input("Usuário: ")
            password = input("Senha: ")
            print("---------------------------")
            if user =="gerente" and password=="mestre001":
                print("Acesso autorizado\n")

                print("---------------------------")
                print("Menu: ")
                print("1 - Fazer cadastro")
                print("2 - Remover usuário")
                print("3 - Visualizar usuário")
                print("---------------------------")
                option = input(">> ")
                if option == "1":
                    RegisterScreen()
                elif option == "2":
                    RemoveScreen()

                elif option=="3":
                    ViewUserScreen()
            else:
                print("Acesso negado")

        else:
            print("Opção inválida")
