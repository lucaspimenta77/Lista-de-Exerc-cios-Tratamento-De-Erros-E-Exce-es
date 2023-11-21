# Escreva uma função que recebe uma string como argumento e retorna o número de vogais contidas nessa string. Use um bloco `try/except` para tratar o caso em que o argumento não é uma string e lance uma exceção personalizada com a mensagem “Argumento inválido”.


def contar_vogais(texto):
    try:
        if not isinstance(texto, str):
            raise TypeError("Argumento inválido - deve ser string")

        vogais = "aeiouAEIOU"
        quantidade_vogais = sum(1 for char in texto if char in vogais)

        return quantidade_vogais
    except TypeError as te:
        raise te


try:
    entrada = input("Digite uma string para contar o número de vogais: ")
    resultado = contar_vogais(entrada)
    print(f"O número de vogais na string é: {resultado}")
except TypeError as e:
    print(f"Erro: {e}")
