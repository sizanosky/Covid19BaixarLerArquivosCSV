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
from datetime import datetime
import locale
import os
import time
import requests

from config import *
from helpers import *

locale.setlocale(locale.LC_ALL, 'pt_br')

print("Hello World!")

if __name__ == "__main__":
    cabecalho("Pesquisa - Dados CORONAVIRUS")

    try:
        arq_time = time.ctime(os.path.getctime(NOME_ARQUIVO))
        local_time = datetime.now()

        with open(NOME_ARQUIVO, 'r') as arq_obj:
            csv.reader(arq_obj)

    except FileNotFoundError:
        print("O arquivo de dados não foi localizado")
        while True:
            resp = input('Você gostaria de fazer o download dos dados mais '
                         'recentes? ("s"-SIM / "n"-NÃO / "q"-ENCERRAR): ')
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

    for linha in leitor_exemplo:
        for pais in pais_ref:
            for data in data_pesquisa:

                # Percorre o arquivo e verifica se há correspondência.
                if linha[2] == pais and linha[3] == data:
                    data = datetime.strptime(data, '%Y-%m-%d')
                    data_format = data.strftime('%d-%m-%Y')

                    # NOVOS CASOS
                    novos_casos = locale.format_string(
                        '%i', int(linha[5].removesuffix('.0')), grouping=True)
                    if ".0" not in novos_casos:
                        pass

                    # TOTAL DE CASOS
                    total_casos = locale.format_string(
                        '%i', int(linha[4].removesuffix('.0')), grouping=True)
                    if ".0" not in total_casos:
                        pass

                    # NOVAS MORTES
                    novas_mortes = locale.format_string(
                        '%i', int(linha[8].removesuffix('.0')), grouping=True)
                    if ".0" not in novas_mortes:
                        pass

                    # TOTAL MORTES
                    total_mortes = locale.format_string(
                        '%i', int(linha[7].removesuffix('.0')), grouping=True)
                    if ".0" not in total_mortes:
                        pass

                    # POPULAÇÃO
                    if linha[48] != '':
                        populacao_str = locale.format_string(
                            '%i', int(linha[48].removesuffix('.0')),
                            grouping=True)
                        populacao_num = int(linha[48].removesuffix('.0'))
                    else:
                        populacao_str = "Não Disponível"

                    # MORTES POR MILHÃO
                    if linha[13] != '':
                        mortes_milhao = locale.format_string(
                            '%.1f', float(linha[13]))
                    else:
                        mortes_milhao = "Não Disponível"

                    # TOTAL VACINADOS
                    if linha[36] != '':
                        total_vacinados = locale.format_string(
                            '%i', int(linha[36].removesuffix('.0')),
                            grouping=True)
                        total_vacinados_num = int(linha[36].removesuffix('.0'))

                        porc_vacinados = \
                            locale.format_string(
                                '%.2f', float(((total_vacinados_num /
                                                populacao_num) * 100)))
                    else:
                        total_vacinados = "Não Disponível"

                    # Mostra os dados na tela.
                    print(f"\n{130 * '_'}"

                          f"\n* Local: {linha[0]}-{linha[2]} | "
                          f"Data: {data_format} | "
                          f"Novos casos(diários): {novos_casos} | "
                          f"Novas mortes(diárias): {novas_mortes} | "
                          f"Total casos: {total_casos}"
                          f"\n- População: {populacao_str}"
                          f"\n- Total mortes: {total_mortes}"

                          f"\n- Mortes/milhão de Habitantes: "
                          f"{mortes_milhao} m/m"

                          f"\n- Total de vacinados (2 doses): {total_vacinados}"
                          f" - ({porc_vacinados}%) da população vacinável."
                          f"\n{130 * '_'}")
