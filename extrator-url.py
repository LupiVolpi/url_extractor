import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile("(http(s)?://)(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida!")

    def get_url_base(self):
        interrogacao_na_url = url.find("?")
        url_base = url[0:interrogacao_na_url]
        return url_base

    def get_url_parametros(self):
        interrogacao_na_url = url.find("?")
        url_parametros = url[interrogacao_na_url + 1: ]
        return url_parametros

    def get_valor_parametro(self, parametro_de_busca):
        indice_do_parametro_de_busca = self.get_url_parametros().find(parametro_de_busca)
        indice_do_valor = indice_do_parametro_de_busca + len(parametro_de_busca) + 1
        indice_do_e_comercial = self.get_url_parametros().find("&", indice_do_valor)
        if indice_do_e_comercial == -1:
            valor = self.get_url_parametros()[indice_do_valor:]
        else:
            valor = self.get_url_parametros()[indice_do_valor: indice_do_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros da URL:" + self.get_url_parametros() + "\n" + "Base da URL:" + self.get_url_base()

    def __eq__(self, outra):
        return self.url == outra.url

url = "https://bytebank.com.br/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)

valor_dolar = 5.50 #1 dólar = 5.50 reais
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
valor_moedaOrigem = extrator_url.get_valor_parametro("moedaOrigem")
valor_moedaDestino = extrator_url.get_valor_parametro("moedaDestino")

print(f"O tamanho da URL é: {len(extrator_url)}")
print(extrator_url)
print("------------------------------------------------------------------------------------------------")
print(f"Deseja-se transferir {valor_quantidade} em {valor_moedaOrigem} para {valor_moedaDestino}")

if valor_moedaOrigem == "real" and valor_moedaDestino == "dolar":
    valor_conversao = int(valor_quantidade) / valor_dolar
    print(f"O valor de R${valor_quantidade} reais é igual a ${str(valor_conversao)} dólares.")
elif valor_moedaOrigem == "dolar" and valor_moedaDestino == "real":
    valor_conversao = int(valor_quantidade) * valor_dolar
    print(f"O valor de ${valor_quantidade} dólares é igual a R${str(valor_conversao)} reais.")
else:
    print(f"Câmbio de {valor_moedaOrigem} para {valor_moedaDestino} não está disponível.")
