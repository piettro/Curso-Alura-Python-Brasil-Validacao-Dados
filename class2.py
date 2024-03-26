from cnpj import *
from document import Document
from validate_docbr import CNPJ

cnpj_generate = CNPJ()
cnpj = cnpj_generate.generate()
cnpj = Cnpj(cnpj)

print(cnpj)

first_cpf = "15316264754"
#print(cpf_um)

#cnpj_exempla = "35379838000112"
#cpf_excample = "11111111112"

#cnpj = CNPJ()
document = Document.creste_document(first_cpf)
print(document)