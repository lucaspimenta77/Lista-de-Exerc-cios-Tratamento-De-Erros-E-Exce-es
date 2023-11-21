#Peça ao usuário para digitar um número inteiro e, em seguida, tente converter esse número em uma string. Trate a exceção que pode ocorrer.

try:
    
    numero_inteiro = int(input("Digite um número inteiro: "))

  
    numero_string = str(numero_inteiro)

   
    print(f"O número {numero_inteiro} convertido para uma string é: {numero_string}")

except ValueError:
   
    print("Erro: Por favor, digite um número inteiro.")
except Exception as e:
  
    print(f"Erro inesperado: {e}")
