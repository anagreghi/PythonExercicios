"""
    Tendo como dado de entrada a altura (h) de uma pessoa, 
    construa um algoritmo que calcule seu peso ideal, 
    utilizando as seguintes fórmulas:
        Para homens: (72.7h) - 58
        Para mulheres: (62.1h) - 44.7
"""

print('Calculadora de peso ideal')
altura = float(input('Informe a altura em metros: '))
print('Informe o sexo')
sexo = input('Digite F para Feminino e M para Masculino: ')

if sexo == 'F' or sexo == 'f':
    peso_ideal = 62.1 * altura - 44.7
elif sexo == 'M' or sexo == 'm':
    peso_ideal = 72.7 * altura - 58
else:
    print('O sexo informado não é válido')
print(f'O seu peso ideal é: {peso_ideal:.2f}')