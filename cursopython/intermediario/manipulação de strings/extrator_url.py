import re

class ExtratorURL:

    def __init__(self, url):
        self.url = url
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip()
    
    def valida_url(self, url):
        if not self.url:
            raise ValueError('URL vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url) 

        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        indice_inte = self.url.find('?')
        url_base = self.url[:indice_inte]
        return url_base
        
    def get_url_parametro(self):
        indice_inte = self.url.find('?')
        url_par = self.url[:indice_inte+1:]
        return url_par
    
    def get_valor_parametro(self, par_busca):
        indice_par = self.get_url_parametro().find(par_busca)
        indice_valor = indice_par + len(par_busca) + 1
        indice_comercial = self.get_url_parametro().find('&', indice_valor)

        if indice_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_comercial]
        return valor


extrator_url = ExtratorURL('https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)
