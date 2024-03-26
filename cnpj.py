from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, document):
        document = str(document)

        if self.cnpj_is_valid(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ invalid!")

    def __str__ (self):
        return self.cnpj_formatted()
    
    def cnpj_formatted(self):
        mask_cnpj = CNPJ()
        return mask_cnpj.mask(self.cnpj)

    def cnpj_is_valid(self, document):
        if len(document) == 14:
            validador = CNPJ()
            return validador.validate(document)
        else:
            raise ValueError("Number of digits invalid")