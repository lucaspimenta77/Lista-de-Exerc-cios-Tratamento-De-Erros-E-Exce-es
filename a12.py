meu_dicionario = {"a": 34, "b": 21, "c": 43, "d":103}

try:
    chave_digitada = input("Digite uma chave: ")

    valor = meu_dicionario[chave_digitada]

    print(f"O valor associado à chave '{chave_digitada}' é: {valor}")

except KeyError:
    print(f"Erro: A chave '{chave_digitada}' não existe no dicionário.")

except Exception as e:
    print(f"Erro inesperado: {e}")
