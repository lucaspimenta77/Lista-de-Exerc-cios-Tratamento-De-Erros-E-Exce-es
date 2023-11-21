def obter_senha():
    while True:
        try:
            senha = input("Digite uma senha com pelo menos 8 caracteres: ")

            if len(senha) < 8:
                raise ValueError("A senha deve ter pelo menos 8 caracteres.")

            return senha

        except ValueError as ve:
            print(f"Erro: {ve}")
            print("Tente novamente.")


senha_digitada = obter_senha()


print("Senha digitada:", senha_digitada)
