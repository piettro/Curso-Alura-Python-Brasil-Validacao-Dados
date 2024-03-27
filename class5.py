from cep import SearchAddress

cep = "06519500"
address = SearchAddress(cep)
print(address)

print(address.access_api())