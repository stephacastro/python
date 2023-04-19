from validate_docbr import CPF, CNPJ

class Documento: 
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de digitos incorreta!')
        
class DocCpf():
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido')
        
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        valida = CPF()
        return valida.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
            
class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ Inválido!!')
    
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        valida_cnpf = CNPJ()
        return valida_cnpf.validate(documento)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
