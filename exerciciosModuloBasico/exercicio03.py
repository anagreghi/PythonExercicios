"""
    Faça um Programa que pergunte quanto você ganha por hora 
    e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês.
"""

print('Calculadora de salário mensal')
valor_hora = float(input('Informe o valor recebido por hora trabalhada: '))
horas_trabalhadas = int(input('Informe o número de horas trabalhadas no mês: '))  
#horas_trabalhadas considero no calculo apenas horas completas.
salario = valor_hora * horas_trabalhadas
print(f'O salário será R${salario:.2f}')

