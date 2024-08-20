"""
    Desenvolva um gerador de tabuada, 
    capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
    O usuário deve informar de qual numero ele deseja ver a tabuada. 
    A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
        ...
    5 X 10 = 50
"""

print('Gerador de tabuada ')
entrada = int(input('Informe a número que deseja ver a tabuada: '))
for i in range(1,11):
    print(f'{entrada} X {i} = {entrada * i}')
    i =+ 1