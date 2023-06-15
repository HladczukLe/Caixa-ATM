class Extrato:
    def __init__(self, cpf_cnpj):
        self.cpf_cnpj=self.format_cpf_cnpj(cpf_cnpj)
        self.money = 0.0
        self.extrato = []

    @staticmethod
    def format_cpf_cnpj(cpf_cnpj):
        cpf_cnpj_formatado = cpf_cnpj.strip().replace(".", "").replace("-", "").replace("/", "")
        if len(cpf_cnpj_formatado) == 11:
            return f"{cpf_cnpj_formatado[:3]}.{cpf_cnpj_formatado[3:6]}.{cpf_cnpj_formatado[6:9]}-{cpf_cnpj_formatado[9:]}"
        elif len(cpf_cnpj_formatado) == 14:
            return f"{cpf_cnpj_formatado[:2]}.{cpf_cnpj_formatado[2:5]}.{cpf_cnpj_formatado[5:8]}/{cpf_cnpj_formatado[8:12]}-{cpf_cnpj_formatado[12:]}"
        return cpf_cnpj_formatado
    
    @staticmethod
    def validar_cpf(cpf_cnpj):
        cpf = cpf_cnpj.replace(".", "").replace("-", "")
        if len(cpf) != 11 or not cpf.isdigit():
            return False

        # Verificação do dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        if resto == 10 or resto != int(cpf[9]):
            return False

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        if resto == 10 or resto != int(cpf[10]):
            return False
        return True
    
    @staticmethod
    def validar_cnpj(cpf_cnpj):
        cnpj = cpf_cnpj.replace(".", "").replace("/", "").replace("-", "")
        if len(cnpj) != 14 or not cnpj.isdigit():
            return False

        # Verificação do dígito verificador
        soma = sum(int(cnpj[i]) * (6 - (i % 8)) for i in range(12))
        digito_1 = 11 - (soma % 11)
        if digito_1 >= 10:
            digito_1 = 0
        if digito_1 != int(cnpj[12]):
            return False

        soma = sum(int(cnpj[i]) * (7 - (i % 8)) for i in range(13))
        digito_2 = 11 - (soma % 11)
        if digito_2 >= 10:
            digito_2 = 0
        if digito_2 != int(cnpj[13]):
            return False
        return True 