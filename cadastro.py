def linha(txt, tam=40):
    print('-' * tam)
    print(txt.center(tam))
    print('-' * tam)


def menu(opcoes):
    linha('MENU PRINCIPAL')

    for i, opcao in enumerate(opcoes, 1):
        print(f'{i} - {opcao}')

    print('-' * 40)

    while True:
        try:
            op = int(input('Sua opção: '))
            if 1 <= op <= len(opcoes):
                return op
            else:
                print('ERRO: opção inválida.')
        except ValueError:
            print('ERRO: digite um número inteiro válido.')
