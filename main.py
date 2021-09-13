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
import locale

import requests

from config import *
from helpers import *

locale.setlocale(locale.LC_ALL, 'pt_br')

print("Hello World!")

if __name__ == "__main__":
    cabecalho("Pesquisa - Dados CORONAVIRUS")

    try:
        with open(NOME_ARQUIVO, 'r') as arq_obj:
            csv.reader(arq_obj)

    except FileNotFoundError:
        print("O arquivo de dados não foi localizado")
        while True:
            resp = input('Você gostaria de fazer o download dos dados mais '
                         'recentes? ("s"-SIM / "n"-NÃO): ')
            if resp.lower() == "s":
                # Requisição para o link do arquivo .csv
                response = requests.get(URL)
                print(f"\nBaixando o arquivo {NOME_ARQUIVO}...\n")

                # Cria um arquivo.csv com dados da URL e salva no local na raiz.
                with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
                    writer = csv.writer(novo_arquivo)  # modulo.método
                    # Itera sobre a variável "response" (modulo.método)
                    for linha in response.iter_lines():
                        writer.writerow(linha.decode('utf-8').split(','))
                    break
            elif resp.lower() == "q":
                print(f"Encerrando...")
                exit()
            elif resp.lower() == "n":
                print(f"\nO arquivo {NOME_ARQUIVO} não foi localizado!\n"
                      f"Este arquivo é necessário para a análise dos dados.\n")
                continue
            else:
                print('Opção invalida, '
                      'digite ("s"-SIM / "n"-NÃO / "q"-ENCERRAR)\n')
                continue

# Abre o arquivo.csv baixado para o diretório raiz do projeto.
with open(NOME_ARQUIVO, 'r') as arq_obj:
    leitor_exemplo = csv.reader(arq_obj)

    # Formata as entradas do usuário.
    pais_ref = pais_entrada()
    data_pesquisa = data_entrada()
    # Armazena os totais de mortes de cada pais.
    totais_mortes = [0]

    for linha in leitor_exemplo:
        for pais in pais_ref:
            for data in data_pesquisa:
                # Percorre o arquivo e verifica se há correspondência.
                if linha[2] == pais and linha[3] == data:
                    novos_casos = locale.format_string(
                        '%i', int(linha[5].removesuffix('.0')), grouping=True)
                    if ".0" not in novos_casos:
                        pass

                    novas_mortes = locale.format_string(
                        '%i', int(linha[8].removesuffix('.0')), grouping=True)
                    if ".0" not in novas_mortes:
                        pass

                    total_casos = locale.format_string(
                        '%i', int(linha[4].removesuffix('.0')), grouping=True)
                    if ".0" not in total_casos:
                        pass

                    total_mortes = locale.format_string(
                        '%i', int(linha[7].removesuffix('.0')), grouping=True)
                    if ".0" not in total_mortes:
                        pass
                    totais_mortes.append(total_mortes)

                    if linha[46] != '':
                        populacao = locale.format_string(
                            '%i', int(linha[46].removesuffix('.0')),
                            grouping=True)
                    else:
                        total_vacinados = "Não Disponível"

                    mortes_milhao = locale.format_string(
                        '%.1f', float(linha[13]))
                    if linha[36] != '':
                        total_vacinados = locale.format_string(
                            '%i', int(linha[36].removesuffix(".0")),
                            grouping=True)
                    else:
                        total_vacinados = "Não Disponível"

                    # Mostra os dados na tela.
                    print(f"\nLocal: {linha[0]}-{linha[2]} | "
                          f"Data: {linha[3]} | "
                          f"Novos casos(diarios): {novos_casos} | "
                          f"Novas mortes(diarias): {novas_mortes} |"
                          f"Total casos: {total_casos} | "
                          f"Total mortes: {total_mortes}"
                          f"\nPopulação: {populacao} | "
                          f"Total mortes/milhão Habitantes: {mortes_milhao} m/m"
                          f"\nTotal de vacinados (2 doses) : {total_vacinados}")
