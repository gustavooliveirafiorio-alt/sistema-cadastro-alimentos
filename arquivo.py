def arquivoExiste(nome):
    try:
        with open(nome, "rt"):
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        with open(nome, "wt+"):
            pass
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'O arquivo {nome} foi criado com sucesso')
def cadastrarAlimento(arquivo, codigo, nome, preco):
    try:
        with open(arquivo, "at") as arq:
            arq.write(f"{codigo};{nome};{preco:.2f}\n")
    except:
        print("Erro ao gravar o alimento.")
    else:
        print("Alimento cadastrado com sucesso!")

def listarAlimentos(nome):
    try:
        with open(nome, "rt") as arq:
            for linha in arq:
                codigo, nome, preco = linha.strip().split(";")
                print(f"Código: {codigo} | Nome: {nome} | Preço: R$ {preco}")
    except:
        print("Erro ao ler o arquivo.")

def codigoExiste(arquivo, codigo_busca):
    try:
        with open(arquivo, "rt") as arq:
            for linha in arq:
                codigo, _, _ = linha.strip().split(";")
                if int(codigo) == codigo_busca:
                    return True
    except:
        pass
    return False

def atualizarAlimento(arquivo, codigo_busca, novo_nome=None, novo_preco=None):
    try:
        linhas = []

        with open(arquivo, "rt") as arq:
            for linha in arq:
                codigo, nome, preco = linha.strip().split(";")

                if int(codigo) == codigo_busca:
                    if novo_nome:
                        nome = novo_nome
                    if novo_preco is not None:
                        preco = f"{novo_preco:.2f}"

                    linhas.append(f"{codigo};{nome};{preco}\n")
                else:
                    linhas.append(linha)

        with open(arquivo, "wt") as arq:
            arq.writelines(linhas)

    except:
        print("\033[31mErro ao atualizar o alimento.\033[m")
    else:
        print("\033[32mAlimento atualizado com sucesso!\033[m")


def deletarAlimento(nome_arquivo, codigo_deletar):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        nova_lista = []
        encontrado = False

        for linha in linhas:
            # Pegamos apenas o código (primeiro item da linha)
            dados = linha.strip().split(";")
            codigo_na_linha = int(dados[0])

            if codigo_na_linha != codigo_deletar:
                nova_lista.append(linha) # Mantém quem não é o código deletado
            else:
                encontrado = True # Se for o código, não adiciona e marca como encontrado

        if encontrado:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.writelines(nova_lista)
            print(f"\033[32mAlimento com código {codigo_deletar} removido com sucesso!\033[m")
        else:
            print(f"\033[31mCódigo {codigo_deletar} não encontrado no arquivo.\033[m")

    except Exception as e:
        print(f"\033[31mErro ao deletar: {e}\033[m")
