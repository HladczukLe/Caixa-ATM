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
        print("1 - Fazer login ")
        print("2 - Fazer cadastro")
        print("3 - Remover usuário")
        print("4 - Visualizar usuário")
        print("---------------------------")
        option = input(">> ")

        if option=="1":
            LoginScreen()

        elif option == "2":
            RegisterScreen()
        elif option == "3":
            RemoveScreen()

        elif option=="4":
            ViewUserScreen()

        else:
            print("Opção inválida")                