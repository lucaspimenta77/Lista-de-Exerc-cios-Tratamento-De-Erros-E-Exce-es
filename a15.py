def dividir_lista(lista, num_partes):
    try:
        if num_partes <= 0 or len(lista) % num_partes != 0:
            raise ValueError("O número de partes não é válido para a lista fornecida.")

        tamanho_parte = len(lista) // num_partes

        partes = [
            lista[i : i + tamanho_parte] for i in range(0, len(lista), tamanho_parte)
        ]

        return partes

    except ValueError as ve:
        print(f"Erro: {ve}")
        return None


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    try:
        num_partes = int(input("Digite o número de partes para dividir a lista: "))
        partes_resultantes = dividir_lista(minha_lista, num_partes)

        if partes_resultantes is not None:
            print("Lista dividida em partes:")
            for parte in partes_resultantes:
                print(parte)
        break

    except ValueError:
        print("Por favor, insira um número inteiro válido.")
