""" 
    Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

lista = []

for i in range(1, 4):
    numero = int(input(f'Informe o {i}º número: '))
    lista.append(numero)

lista.sort(reverse=True)
print(lista)