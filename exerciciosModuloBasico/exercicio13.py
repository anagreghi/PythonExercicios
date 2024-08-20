"""
Tamanho de strings. 
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
Modelo:
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

string_1 = input('Informe uma string: ')
string_2 = input('Informe outra string: ')
tam_string_1 = len(string_1)
tam_string_2 = len(string_2)

print(f'Tamanho de "{string_1}": {tam_string_1} caracteres')
print(f'Tamanho de "{string_2}": {tam_string_2} caracteres')

if tam_string_1 == tam_string_2: 
    print('As duas strings possuem o mesmo tamanhos')
    if string_1 == string_2:    
        print('As duas strings possuem o mesmo conteúdo')
    else:
        print('As duas strings possuem conteúdos diferentes')

else:
    print('As duas strings são de tamanhos diferentes')
    print('As duas strings possuem conteúdos diferentes')