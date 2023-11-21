def dividir_numeros(a, b):
    try:
        resultado = a / b
        return resultado

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        return None

    except TypeError:
        print("Erro: Certifique-se de que ambos os números são do tipo numérico.")
        return None

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None


while True:
    try:
        num1 = float(input("Digite o numerador: "))
        num2 = float(input("Digite o denominador: "))

        resultado_divisao = dividir_numeros(num1, num2)

        if resultado_divisao is not None:
            print("Resultado da divisão:", resultado_divisao)

        break

    except ValueError:
        print("Por favor, insira um número válido.")
