from random import randint

# parametro é um dado de entrada
def saudacao(nome):
    print(f"Boa noite, {nome}!")


def saudar():
    print("Boa noite!")


saudacao("Bruno")
saudar()


def somar(numero1, numero2):
    return numero1 + numero2


resultado = somar(5, 10)
print(resultado)


# def calcular_imc(peso, altura, nome):
#     imc = peso / (altura * altura)
#     return f"{nome} seu IMC é: {round(imc, 2)}"

def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc >= 18.5 and imc < 24.9:
        classificacao = "Peso normal"
    elif imc >= 25 and imc < 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    return imc, classificacao


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
nome = input("Digite seu nome: ")
# print(calcular_imc(peso, altura, nome))
imc, classificacao = calcular_imc(peso, altura)  # unpacking
print(imc, classificacao)

# unpacking de tuplas
# pessoa = "Luiz", 25
# print(type)
# nome, idade = pessoa


def gerar_numero_secreto():
    return randint(1, 100)


def jogo_adivinhacao(numero):
    numero_secreto = gerar_numero_secreto()
    if numero < numero_secreto:
        print("Muito baixo! Tente novamente")
    elif numero > numero_secreto:
        print("Muito alto! Tente novamente")
    else:
        print("Você adivinhou o número")


jogo_adivinhacao(50)