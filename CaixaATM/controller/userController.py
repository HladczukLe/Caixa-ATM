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

class UserController:
    def __init__(self):
        pass

    def updateJson(self):
        with open(userDirectory, 'w') as updateUserFile:
            json.dump(userList, updateUserFile, indent=4)
        with open(extratoDirectory, 'w') as updateExtratoFile:
            json.dump(extratoList, updateExtratoFile, indent=4)

    def login(self,cpf_cnpj,password):
        self.cpf_cnpj = format_cpf_cnpj(cpf_cnpj)
        for user in userList:
            if user['cpf_cnpj'] == self.cpf_cnpj and user['password'] == password:
                print(f"Login concluído! Bem vindo(a) {user['name']}!")
                return user
        print("Usuário ou senha incorretos.")
            
    def depositar(self, loggedUser):
        self.valor = float(input("Qual o valor a ser depositado? "))
        for user in userList:
            for conta in extratoList:
                if user['cpf_cnpj'] == loggedUser['cpf_cnpj'] and self.valor>0 and conta['cpf_cnpj']==loggedUser['cpf_cnpj']:
                    conta['money'] += self.valor
                    conta['extrato'].append(f"Depositou R${self.valor}")
                    self.updateJson()
                    print("Operação concluída")

    def sacar(self, loggedUser):
        self.valor = float(input("Qual o valor a ser sacado? "))
        for user in userList:
            for conta in extratoList:
                if user['cpf_cnpj'] == loggedUser['cpf_cnpj'] and conta['cpf_cnpj']==loggedUser['cpf_cnpj']:
                    if self.valor >0 and self.valor <= conta['money']:
                        conta['money']-= self.valor
                        conta['extrato'].append(f"Saque R${self.valor}")
                        self.updateJson()
                        print("Operação concluída")
                        return
        print(f"Você não tem saldo suficiente!")

    def verSaldo(self, loggedUser):
        for user in userList:
            for conta in extratoList:
                if user['cpf_cnpj'] == loggedUser['cpf_cnpj'] and conta['cpf_cnpj']==loggedUser['cpf_cnpj']:
                    print(f"{loggedUser['name']}, você tem R${conta['money']} disponível")

    def consultarExtrato(self,loggedUser):
        for conta in extratoList:
            if loggedUser['cpf_cnpj'] == conta["cpf_cnpj"]:
                print(conta['extrato'])

    def solicitarCredito(self,  loggedUser):
        self.valor = float(input("Insira o valor a ser solicitado: "))
        for user in userList:
            for conta in extratoList:
                if len(loggedUser['cpf_cnpj'])==14:
                    if self.valor > 0.0 and self.valor<5000:
                        conta['money'] += self.valor
                        conta['extrato'].append(f"Solicitação de crédito: +R${self.valor}")
                        self.updateJson()
                        print("operação concluída")
                        return True
                    print("Valor alto demais. Pessoa física pode solicitar até 5000 reais")
                    return False
                elif len(loggedUser['cpf_cnpj'])==18:
                    if self.valor > 0.0 and self.valor<10000:
                        conta['money'] += self.valor
                        conta['extrato'].append(f"Solicitação de crédito: +R${self.valor}")
                        self.updateJson()
                        print("operação concluída")
                        return True
                    print("Valor alto demais. Pessoa jurídica pode solicitar até 10000 reais")
                    return False