url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

# O separador da url base e dos parâmetros da url
interrogacao_na_url = url.find("?")
url_base = url[0:interrogacao_na_url]
print(url_base)
url_parametros = url[interrogacao_na_url + 1: ]
print(url_parametros)

# O que obtém o valor dos parâmetros dinamicamente
parametro_de_busca = "moedaOrigem"
indice_do_parametro_de_busca = url_parametros.find(parametro_de_busca)
indice_do_valor = indice_do_parametro_de_busca + len(parametro_de_busca) + 1

indice_do_e_comercial = url_parametros.find("&", indice_do_valor)
if indice_do_e_comercial == -1:
    valor = url_parametros[indice_do_valor: ]
else:
    valor = url_parametros[indice_do_valor: indice_do_e_comercial]

print(valor)

