#Faça um programa, com uma função que necessite de um parâmetro “número”. A função retorna o valor de
#caractere ‘P’, se seu valor for positivo, e ‘N’, se seu valor for zero ou negativo.

def verifica_numero(numero):
    if numero > 0:
        return 'P'  
    else:
        return 'N'  

numero = float(input("Digite um número: "))
resultado = verifica_numero(numero)
print(f"O resultado é: {resultado}")
