"""
    Faça um Programa que peça dois números e imprima o maior deles.
"""

print('Encontrando o maior número entre dois números')
numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número: '))

if numero_1 > numero_2:
    print(f'O número: {numero_1} é maior')
elif numero_1 < numero_2:
    print(f'O número: {numero_2} é maior')
else:
    print('Os números são iguais')