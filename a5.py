try:
    with open("trabalho.txt", "w") as arquivo:
        arquivo.write("Conteudo do trabalho.")

except FileExistsError as e:
    print(f"Erro: {e}. O arquivo ja existe.")
except Exception as e:
    print(f"Erro inesperado: {e}")
