try:
    valor = int(input("Digite um número inteiro: "))
    resultado = 10 / valor
    print("Resultado:", resultado)

except Exception as e:
    print("Ocorreu uma exceção:", e)
    print("Por favor, forneça um valor válido.")
