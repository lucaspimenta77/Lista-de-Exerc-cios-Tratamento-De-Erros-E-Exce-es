# Escreva uma função que recebe um número inteiro positivo como argumento e retorna o fatorial desse número. Use um bloco `try/except` para tratar o caso em que o argumento é negativo ou não é um inteiro e lance uma exceção personalizada com a mensagem “Argumento inválido”.


def calcular_fatorial(numero):
    try:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("Argumento inválido - deve ser um inteiro positivo")

        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i

        return resultado
    except ValueError as ve:
        raise ve


try:
    numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
