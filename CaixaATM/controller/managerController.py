from model.user import User
from model.extrato import Extrato
import json

userDirectory = "database\\users.json"
extratoDirectory = "database\\extrato.json"

with open(userDirectory) as usersFile:
    userList = json.load(usersFile)
with open(extratoDirectory) as extratoFile:
    extratoList = json.load(extratoFile)

def format_cpf_cnpj(cpf_cnpj):
        cpf_cnpj_formatado = cpf_cnpj.strip().replace(".", "").replace("-", "").replace("/", "")
        if len(cpf_cnpj_formatado) == 11:
            return f"{cpf_cnpj_formatado[:3]}.{cpf_cnpj_formatado[3:6]}.{cpf_cnpj_formatado[6:9]}-{cpf_cnpj_formatado[9:]}"
        elif len(cpf_cnpj_formatado) == 14:
            return f"{cpf_cnpj_formatado[:2]}.{cpf_cnpj_formatado[2:5]}.{cpf_cnpj_formatado[5:8]}/{cpf_cnpj_formatado[8:12]}-{cpf_cnpj_formatado[12:]}"
        return cpf_cnpj_formatado

class ManagerController:
    def __init__(self):
        pass

    def registerUser(self,name,cpf_cnpj,adress,phone,password):
        if not User.validar_cpf(cpf_cnpj) and not User.validar_cnpj(cpf_cnpj):
            print("CPF ou CNPJ inválido")
            return
        else:
            newUser = vars(User(name,cpf_cnpj,adress,phone,password))
            userList.append(newUser)
            extratoList.append(vars(Extrato(newUser['cpf_cnpj'])))
            self.updateJson()
            print(f"Usuário cadastrado! Bem vindo(a) {name}")

    def removeUser(self,cpf_cnpj,password):
        self.cpf_cnpj = format_cpf_cnpj(cpf_cnpj)
        for i, user in enumerate(userList):
            if user['cpf_cnpj'] == self.cpf_cnpj and user['password'] == password:
                for j, conta in enumerate(extratoList):
                    if conta["cpf_cnpj"]==self.cpf_cnpj and conta['money']== 0.0:
                        userList.pop(i)
                        extratoList.pop(j)
                        self.updateJson()
                        print('Usuário removido')
                        return
                    elif conta["cpf_cnpj"]==self.cpf_cnpj and conta['money']> 0.0:
                        print("Zere a conta bancária antes de remover o usuário")
                        return
        print("Usuário não encontrado")
       
    def viewUser(self,cpf_cnpj,password):
        self.cpf_cnpj = format_cpf_cnpj(cpf_cnpj)

        for user in userList:
            if user['cpf_cnpj'] == self.cpf_cnpj and user['password']==password:
                print(f'----------------Usuário----------------')
                print(f'Nome: {user["name"]}')
                print(f'CPF/CNPJ: {user["cpf_cnpj"]}')
                print(f'Endereço: {user["adress"]}')
                print(f'Telefone: {user["phone"]}')
                print(f'---------------------------------------')
                return
        print("Usuário não encontrado")
    
    def updateJson(self):
            with open(userDirectory, 'w') as updateUserFile:
                json.dump(userList, updateUserFile, indent=4)
            with open(extratoDirectory, 'w') as updateExtratoFile:
                json.dump(extratoList, updateExtratoFile, indent=4)