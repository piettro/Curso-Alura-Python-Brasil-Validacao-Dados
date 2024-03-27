import requests

class SearchAddress:
    def __init__(self, cep):
        cep = str(cep)

        if self.cep_is_valid(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Invalid!")

    def cep_is_valid(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
    
    def access_api(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        response = requests.get(url)
        response = response.json()
        return (
            response['bairro'],
            response['localidade'],
            response['uf'],
        )