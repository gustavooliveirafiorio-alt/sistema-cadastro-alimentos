# sistema-cadastro-alimentos
SISTEMA RESTAURANTE
from time import sleep
from arquivo import (
    arquivoExiste,
    criarArquivo,
    cadastrarAlimento,
    listarAlimentos,
    atualizarAlimento,
    deletarAlimento
)
from cadastro import menu, linha

ARQ = "alimentos_cadastradas.txt"

if not arquivoExiste(ARQ):
    criarArquivo(ARQ)

while True:
    opcao = menu([
        "Ver alimentos cadastrados",
        "Cadastrar novo alimento",
        "Atualizar alimento",
        "Deletar um alimento",
        "Sair do sistema"
    ])

    if opcao == 1:
        linha("ALIMENTOS CADASTRADOS")
        listarAlimentos(ARQ)

    elif opcao == 2:
        linha("CADASTRAR NOVO ALIMENTO")
        try:
            codigo = int(input("Código: "))
            nome = input("Nome: ").strip().upper()
            preco = float(input("Preço: R$ "))
        except ValueError:
            print("\033[31mERRO: Código e Preço devem ser numéricos!\033[m")
        else:
            cadastrarAlimento(ARQ, codigo, nome, preco)
            print(f"Alimento {nome} cadastrado com sucesso!")

    elif opcao == 3:
        linha("ATUALIZAR ALIMENTO")
        try:
            from arquivo import codigoExiste
            codigo = int(input("Código do alimento: "))
        except (ValueError, ImportError):
            print("\033[31mErro no código ou função inexistente!\033[m")
        else:
            if not codigoExiste(ARQ, codigo):
                print("\033[31mERRO: alimento não encontrado.\033[m")
            else:
                nome = input("Novo nome (Enter para manter): ").strip().upper()
                preco_input = input("Novo preço (Enter para manter): ")

                novo_preco = None
                if preco_input != "":
                    try:
                        novo_preco = float(preco_input)
                    except ValueError:
                        print("\033[31mPreço inválido!\033[m")
                        continue

                atualizarAlimento(
                    ARQ,
                    codigo,
                    novo_nome=nome if nome else None,
                    novo_preco=novo_preco
                )

    elif opcao == 4:
        linha("DELETAR UM ALIMENTO")
        try:
            codigo = int(input("Código do alimento que deseja deletar: "))
            deletarAlimento(ARQ, codigo)
        except ValueError:
            print("\033[31mCódigo inválido!\033[m")

    elif opcao == 5:
        linha("Saindo do sistema... Até logo!")
        break

    else:
        print("\033[31mERRO: Digite uma opção válida!\033[m")

    sleep(1)
