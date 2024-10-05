#Crie uma calculadora utilizando funções
# a.
# Obrigatoriamente você deve ter funções: somar; subtrair; multiplicar e dividir
# i Todas recebem 2 números como parâmetro de entrada

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Erro! Divisão por zero."
    return num1 / num2

def calculadora():
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"Resultado: {somar(num1, num2)}")
    elif escolha == '2':
        print(f"Resultado: {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Opção inválida.")
        
calculadora()
