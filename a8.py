# Escreva uma função que recebe uma lista de strings como argumento e retorna uma nova lista com estas strings ordenadas alfabeticamente. Use um bloco `try/except` para tratar o caso em que a lista contém algum elemento que não é uma string e lance uma exceção personalizada com a mensagem “Lista inválida”.


def ordenar_strings(lista):
    try:
        if not all(isinstance(elemento, str) for elemento in lista):
            raise ValueError("Lista inválida - deve conter apenas strings")

        lista_ordenada = sorted(lista)

        return lista_ordenada
    except ValueError as ve:
        raise ve


try:
    lista_strings = ["banana", "abacaxi", "laranja", "uva", "mamão", "leite", "morango"]
    resultado = ordenar_strings(lista_strings)
    print(f"Lista ordenada alfabeticamente: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
