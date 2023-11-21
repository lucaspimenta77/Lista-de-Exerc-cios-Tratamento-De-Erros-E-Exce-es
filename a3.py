# Escreva uma função que recebe uma lista de números como argumento e retorna a soma dos elementos da lista. Use um bloco `try/except` para tratar o caso em que a lista contém algum elemento que não é um número e lance uma exceção personalizada com a mensagem “Lista inválida”.


def soma_lista_numeros(lista):
    try:
        total = sum(map(float, lista))
        return total
    except (ValueError, TypeError):
        raise Exception("Lista inválida - contém elementos que não são números")


try:
    lista_numeros = input("Digite uma lista de números separados por espaços: ").split()
    resultado = soma_lista_numeros(lista_numeros)
    print(f"A soma dos números na lista é: {resultado}")
except Exception as e:
    print(f"Erro: {e}")
