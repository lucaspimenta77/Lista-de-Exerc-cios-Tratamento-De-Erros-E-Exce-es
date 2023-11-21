# Escreva um programa que solicita ao usuário um nome de arquivo e tenta abri-lo para leitura. Use um bloco `try/except` para tratar o caso em que o arquivo não existe ou não pode ser aberto e lance uma exceção personalizada com a mensagem “Arquivo inválido”.


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo:\n{conteudo}")
    except (FileNotFoundError, IOError):
        raise Exception("Arquivo inválido - não encontrado ou não pode ser aberto")


try:
    nome_do_arquivo = input("Digite o nome do arquivo para leitura: ")
    ler_arquivo(nome_do_arquivo)
except Exception as e:
    print(f"Erro: {e}")
