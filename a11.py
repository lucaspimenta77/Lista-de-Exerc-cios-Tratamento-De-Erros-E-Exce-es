# Crie um programa que leia as configurações de um arquivo e trate exceções caso o arquivo contenha erros de formatação.


def ler_configuracoes(arquivo):
    config = {}
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                chave, valor = linha.strip().split("=")
                config[chave.strip()] = valor.strip()
        return config
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except ValueError:
        print(
            f"Erro de formatação no arquivo '{arquivo}'. Certifique-se de que está no formato correto."
        )
    except Exception as e:
        print(f"Erro inesperado: {e}")


try:
    arquivo_config = "config.txt"
    configuracoes = ler_configuracoes(arquivo_config)

    if configuracoes:
        print("Configurações lidas com sucesso:")
        for chave, valor in configuracoes.items():
            print(f"{chave}: {valor}")

except Exception as e:
    print(f"Erro: {e}")
