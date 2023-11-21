try:
    with open("numero.txt", "r") as arquivo:
        l = arquivo.readline()

        numero = int(l)

except FileNotFoundError as fnfe:
    print(f"Erro: {fnfe}")
    print("Certifique-se de que o arquivo existe.")

except ValueError as ve:
    print(f"Erro: {ve}")
    print("Certifique-se de que o conteúdo do arquivo é um número inteiro válido.")

except Exception as e:
    print(f"Erro inesperado: {e}")

else:
    print("Operação concluída com sucesso.")

finally:
    print("Fim do programa.")
