"""
    Faça um Programa que converta metros para centímetros.
"""

print('Conversor de metros para centímetros')
metros = input('Informe o valor em metros a ser convertido para centímetros: ')
metros_float = float(metros)
print(f'metros float: {metros_float}')
centimetros = metros_float * 100
print(f'{metros_float} metros equivalem a {centimetros:.0f} centímetros')