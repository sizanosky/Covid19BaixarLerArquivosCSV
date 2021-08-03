"""
* Módulo 20 - Baixar e ler um arquivo CSV
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 24/05/2021

  Programa em Python 3 para ler e gravar arquivos CSV, a URL com os dados
 tem como base os dados da pandemia do CORONAVIRUS retirados do site
 https://ourworldindata.org/
"""

import csv
import requests
import locale
from config import URL, ARQUIVO_CSV
from helpers import *

locale.setlocale(locale.LC_ALL, 'pt_br')

print("Hello World!")

if __name__ == "__main__":
    print("\n++++++ Dados CORONAVIRUS ++++++\n")

# Requisição para o link do arquivo .csv
response = requests.get(URL)
mens_carregando()


# Criando um arquivo com dados da URL e salvando no PC local.
with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
    writer = csv.writer(novo_arquivo)  # modulo.metodo
    for linha in response.iter_lines():  # Itera a resposta(modulo.metodo)
        writer.writerow(linha.decode('utf-8').split(','))  # Escreve uma linha

# Abrir um arquivo .csv a partir do projeto raiz.
with open(ARQUIVO_CSV, 'r') as arq_obj:
    leitor_exemplo = csv.reader(arq_obj)

    mens_input = f"Digite o(s) nome do país(es) que você deseja obter os dados da pandemia e comparar os dados.\n"\
                 f"Use o nome do país respeitando os identificadores universais(grafia na lingua Inglesa).\n"\
                 f"Use apenas virgulas para separar os nomes ex: Brazil,Portugal,India.\n\n" \
                 f"País(es): "
    pais_ref = list(input(mens_input).split(','))
    data_pesquisa = input('Data da pesquisa (AAAA-MM-DD): ')

    for linha in leitor_exemplo:
        for nome_pais in pais_ref:
            pais = nome_pais.title()
            # Percorre o arquivo e verifica em qual linha correspondem (linha[2] = pais_ref, linha[3] =  data)
            if linha[2] == pais and linha[3] == data_pesquisa:

                novos_casos = locale.format_string('%i', int(linha[5].removesuffix('.0')), grouping=True)
                novas_mortes = locale.format_string('%i', int(linha[8].removesuffix('.0')), grouping=True)
                total_casos = locale.format_string('%i', int(linha[4].removesuffix('.0')), grouping=True)
                total_mortes = locale.format_string('%i', int(linha[7].removesuffix('.0')), grouping=True)
                populacao = locale.format_string('%i', int(linha[44].removesuffix('.0')), grouping=True)

                print(f"\nLocal: {linha[0]}-{linha[2]} | Data: {linha[3]} | "
                      f"Novos casos: {novos_casos} | Novas mortes: {novas_mortes} |"
                      f"Total casos: {total_casos} | Total mortes: {total_mortes}"
                      f"\nPopulação: {populacao}")
