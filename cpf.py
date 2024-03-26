from validate_docbr import CPF

class Cpf:
    def __init__(self, document):
        document = str(document)

        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError("CPF invalid!")

    def __str__ (self):
        return self.cpf_formatted()
    
    def cpf_formatted(self):
        mask_cpf = CPF()
        return mask_cpf.mask(self.cpf)

    def cpf_is_valid(self, document):
        if len(document) == 11:
            validador = CPF()
            return validador.validate(document)
        else:
            raise ValueError("Number of digits invalid")