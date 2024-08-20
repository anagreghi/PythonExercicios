"""
try -> tentar executar o código
except -> ocorreu um erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')
# if numero_str.isdigit():
#     numero_float = float(numero_str) #convertendo a string numero para float
#     print(f'O dobro de {numero_float} é {numero_float * 2}')
# else:
#     print('Isso não é um número inteiro')

try:
    print('STR', numero_str.isdigit())
    numero_float = float(numero_str) #convertendo a string numero para float
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um número inteiro')
