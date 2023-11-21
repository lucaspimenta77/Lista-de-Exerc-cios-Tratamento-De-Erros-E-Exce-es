# Escreva um programa que solicita ao usuário uma data no formato "dd/mm/aaaa" e verifica se ela é válida. Use um bloco `try/except` para tratar o caso em que o usuário digita uma data inválida e lance uma exceção personalizada com a mensagem “Data inválida”.


def validar_data(data_str):
    try:
        dia, mes, ano = map(int, data_str.split("/"))
        data = datetime.datetime(ano, mes, dia)
        return True
    except ValueError:
        raise Exception("Data inválida")


import datetime

try:
    data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
    if validar_data(data_usuario):
        print("Essa data válida!")
except Exception as e:
    print(f"Erro: {e}")
