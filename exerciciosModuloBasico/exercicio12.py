"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""
print('Verificador de números primos')
numero = int(input('Informe o número a ser verificado: '))
primo = 0
for contador in range(2, numero):
    if (numero % contador == 0):       
        primo += 1
if (primo == 0):
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')
