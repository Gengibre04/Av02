#Em outra pasta, crie um arquivo: 
#controlador_usuario que contém a função:- autenticar recebendo como parâmetro login e 
#senha-Dentro dessa função temos uma lista de 
#dicionários com:-Verifique se o login e senha enviado é 
#compatível com algum desses
#● Crie uma função que receba uma string e retorne o número de vogais 
#presentes na string.
# ● Escreva uma função que calcule o fatorial de um número inteiro 
#não-negativo.
# ● Escreva uma função que receba um número e retorne True se ele for primo e 
#False caso contrário.
# ● Crie uma função que receba uma lista de números e retorne a soma de todos 
#os elementos da lista.
# ● Crie uma função que receba uma string e retorne o número de palavras na 
#string.
#● Crie uma função que receba uma lista de números e retorne a média.
# ● Crie uma função que converta uma temperatura de Celsius para Fahrenheit e 
#vice-versa.
# ● Crie uma função que receba um email e retorna se ele possui ‘@’
 
 
usuarios = [
    {"username": "teste", "password": "admin"},
    {"username": "teste2", "password": "admin2"},
    {"username": "teste3", "password": "admin3"},
    {"username": "teste4", "password": "admin4"},
]
 
def autenticação(login, senha):
    for usuario in usuarios:
        if usuario["username"] == login and usuario["password"] == senha:
            return True
    return False
login = input("Digite seu nome de usuário:")
senha = input("Digite sua senha:")
if autenticação(login,senha):
    print("Login inserido corretamente")
else:
    print("falha no login, senha ou nome inserido incorretamente!")
