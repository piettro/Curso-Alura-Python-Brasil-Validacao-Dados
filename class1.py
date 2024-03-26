from cpf import *
from validate_docbr import CPF

cpf_generate = CPF()
cpf = cpf_generate.generate()
cpf = Cpf(cpf)

print(cpf)