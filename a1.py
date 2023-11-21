# Escreva uma função que recebe dois números como argumentos e retorna a divisão do primeiro pelo segundo. Use um bloco try/except para tratar o caso em que o segundo número é zero e lance uma exceção personalizada com a mensagem "Divisão por zero não permitida".


def divisao_personalizada(numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        raise ValueError("Divisão por zero não permitida")


try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = divisao_personalizada(numero1, numero2)
    print(f"O resultado da divisão é: {resultado}")

except ValueError as ve:
    print(f"Erro: {ve}")

except Exception as e:
    print(f"Erro inesperado: {e}")
