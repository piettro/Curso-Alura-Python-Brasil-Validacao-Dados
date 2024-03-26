from validate_docbr import CPF, CNPJ

class Document:

    @staticmethod
    def creste_document(document):
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Number of digits invalid!")

class DocCpf:
    def __init__(self, document):
        if self.validate(document):
            self.cpf = document
        else:
            raise ValueError("CPF Invalid!")

    def __str__(self):
        return self.format()

    def validate(self, document):
        cpf_validate = CPF()
        return cpf_validate.validate(document)

    def format(self):
      mask = CPF()
      return mask.mask(self.cpf)

class DocCnpj:
    def __init__(self, document):
        if self.validate(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ Invalid!")

    def __str__(self):
        return self.format()

    def validate(self, document):
        cnpj_validate = CNPJ()
        return cnpj_validate.validate(document)

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)