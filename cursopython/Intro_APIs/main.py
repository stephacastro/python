from acesso_cep import BuscaEndereco
import requests

cep = 62232974
obj_cep = BuscaEndereco(cep)

""" site_cep = requests.get('https://viacep.com.br/ws/85181100/json/')

print(site_cep.text)  """

bairro, cidade, uf = obj_cep.acesso_api()
print(bairro, cidade, uf)