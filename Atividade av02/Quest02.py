#Escreva uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def contar_digitos(numero):
    return len(str(abs(numero)))

numero = int(input("Digite um número inteiro: "))
quantidade_digitos = contar_digitos(numero)
print(f"O número {numero} tem {quantidade_digitos} dígitos.")
