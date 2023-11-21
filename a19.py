def buscar_elemento(lista, elemento):
    try:
        indice = lista.index(elemento)
    except ValueError:
        print(f"Erro: O elemento '{elemento}' não foi encontrado na lista.")
    except TypeError:
        print("Erro: Certifique-se de que a lista é válida.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    else:
        print(f"Elemento '{elemento}' encontrado no índice {indice} da lista.")


minha_lista = [10, 21, 40, 36, 5, 44, 7, 32]

while True:
    try:
        elemento_procurado = int(input("Digite o elemento a ser buscado na lista: "))
        buscar_elemento(minha_lista, elemento_procurado)
        break

    except ValueError:
        print("Por favor, insira um número válido.")
