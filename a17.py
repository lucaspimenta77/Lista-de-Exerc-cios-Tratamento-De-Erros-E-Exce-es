try:
    while True:
        print("Executando...")

except KeyboardInterrupt:
    # (Ctrl C)
    print("\nLoop interrompido pelo usuário.")
finally:
    print("Fim do programa.")
