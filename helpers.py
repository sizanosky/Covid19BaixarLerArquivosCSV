"""
/* Helpers */

Funções utilizadas em main.py

Data criação: 01-08-2021
"""


def cabecalho(texto):
    """
    Função para formatar um cabeçalho para o programa.
    :return: string
    """
    print(f'{"=" * len(texto) + 10 * "="}')
    print(f'{"*" * len(texto) + 10 * "*"}')
    print(f"++++ {texto} ++++")
    print(f'{"*" * len(texto) + 10 * "*"}')
    print(f'{"=" * len(texto) + 10 * "="}')
    print()


def pais_entrada():
    """
    Função que recebe a entrada do usuário e trata os dados da lista criada.
    :return: Retorna uma lista com a entrada do usuário já tratada
    """
    mens_input = f"Digite o(s) nome do país(es) que você deseja obter os " \
                 f"dados da pandemia e comparar os dados.\n"\
                 f"Use o nome do país respeitando os identificadores " \
                 f"universais(grafia na lingua Inglesa).\n"\
                 f"Use apenas virgulas para separar os nomes " \
                 f"ex: Brazil,Portugal,India.\n\n" \
                 f"País(es): "
    lista_pais = list(input(mens_input).split(','))
    pais_ref = []

    for pais in lista_pais:
        pais_ref.append(pais.lstrip().title())

    return pais_ref

def data_entrada():
    """
    Função que recebe a entrada do usuário, cria uma lista
    e trata os dados da lista criada.
    :return: Retorna uma lista com a entrada do usuário já tratada
    :return:
    """
    mens_input = 'Data(s) para pesquisa (AAAA-MM-DD): '
    lista_data = list(input(mens_input).split(','))
    data_pesquisa = []

    for data in lista_data:
        data_pesquisa.append(data.lstrip())

    return data_pesquisa
