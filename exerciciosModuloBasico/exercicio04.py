"""
    Tendo como dados de entrada a altura de uma pessoa,
    construa um algoritmo que calcule seu peso ideal, 
    usando a seguinte fórmula: (72.7*altura) - 58
"""

print('Calculadora de peso ideal')
altura = float(input('Informe a altura em metros: '))
peso_ideal = 72.7 * altura - 58
print(f'O seu peso ideal é: {peso_ideal:.2f}')