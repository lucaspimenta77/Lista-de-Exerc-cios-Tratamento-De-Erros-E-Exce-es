try:
    minha_lista = [1, 2, 3, 4, 5, 7, 10, 13]

    indice = int(input("Digite um índice para acessar o elemento na lista: "))

    elemento = minha_lista[indice]

    print(f"O elemento na posição {indice} é: {elemento}")

except IndexError:
    print("Erro: O índice está fora dos limites da lista.")

except ValueError:
    print("Erro: Por favor, digite um valor inteiro como índice.")

except Exception as e:
    print(f"Erro inesperado: {e}")
