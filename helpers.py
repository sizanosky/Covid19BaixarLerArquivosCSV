def mens_carregando(cont=0):
    """
    Exibe uma mensagem enquanto a aplicação carrega.
    :return:
    """
    from time import sleep

    print(f"- Carregando aplicação.", end='')
    while cont <= 5:
        print(f".", end='')
        sleep(1)
        cont += 1
    print(f".\n")
