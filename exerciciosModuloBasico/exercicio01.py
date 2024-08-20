# Faça um Programa que peça dois números inteiros e imprima a soma.
try:
    numero1 = int(input('Digite o primeiro número inteiro: '))
    numero2 = int(input('Digite o segundo número inteiro: '))
    soma = numero1 + numero2
    print(f'A soma do número {numero1} com o {numero2} é: {soma}')
except:
    print('Você não informou um número inteiro')



