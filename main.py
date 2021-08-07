"""
* Módulo 20 - Baixar e ler um arquivo CSV
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 24/05/2021

  Programa em Python 3 para ler e gravar arquivos CSV, a URL com os dados
 tem como base os dados da pandemia do CORONAVIRUS retirados do site
 https://ourworldindata.org/
"""

import matplotlib.pyplot as plt
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

    pais_ref = pais_entrada()
    data_pesquisa = data_entrada()

    for linha in leitor_exemplo:
        for pais in pais_ref:
            for data in data_pesquisa:
                # Percorre o arquivo e verifica se há correspondência (linha[2] = pais_ref, linha[3] =  data)
                if linha[2] == pais and linha[3] == data:
                    novos_casos = locale.format_string('%i', int(linha[5].removesuffix('.0')), grouping=True)
                    novas_mortes = locale.format_string('%i', int(linha[8].removesuffix('.0')), grouping=True)
                    total_casos = locale.format_string('%i', int(linha[4].removesuffix('.0')), grouping=True)
                    total_mortes = locale.format_string('%i', int(linha[7].removesuffix('.0')), grouping=True)
                    populacao = locale.format_string('%i', int(linha[44].removesuffix('.0')), grouping=True)
                    mortes_milhao = locale.format_string('%.1f', float(linha[13]))
                    if linha[38] != '':
                        total_vacinados = locale.format_string('%i', int(linha[38].removesuffix(".0")), grouping=True)
                    else:
                        total_vacinados = "Não Disponível"

                    print(f"\nLocal: {linha[0]}-{linha[2]} | Data: {linha[3]} | "
                          f"Novos casos: {novos_casos} | Novas mortes: {novas_mortes} |"
                          f"Total casos: {total_casos} | Total mortes: {total_mortes}"
                          f"\nPopulação: {populacao} | Total mortes/milhão Habitantes: {mortes_milhao} m/m"
                          f"\nTotal de vacinados (2 doses) : {total_vacinados}")

plt.plot(pais_ref, data_pesquisa)
plt.show()
