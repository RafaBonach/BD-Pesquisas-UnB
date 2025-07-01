import os

def clear():
    """Limpa o terminal, tanto no Windows quanto no Linux"""
    os.system('cls' if os.name == 'nt' else 'clear')


def input_choice(n_options:int):
    """
    Considera que o menu vai de 0 a n_options -1

    :param n_options: número de escolhas possíveis

    :returns: -1 se a escolha for inválida
    :returns: valor da escolha se for válida
    """

    choice = input()

    if not choice.isnumeric():
        return -1
    
    choice = int(choice)

    if choice < 0 or choice > n_options -1:
        return -1
    
    return choice


def print_menu(options):
    for i in range(len(options)):
        print(f"{i} - {options[i]}")
