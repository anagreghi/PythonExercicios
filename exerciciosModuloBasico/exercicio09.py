"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".

"""
print('Digite 1 para SIM e 2 para NÃO')
classificacao = 0
resposta = int(input('Telefonou para a vítima? '))
print(f'a resposta foi {resposta}')
if resposta == 1:
    classificacao += 1
resposta = int(input('Esteve no local do crime? '))
if resposta == 1:
    classificacao += 1  
resposta = int(input('Mora perto da vítima? '))
if resposta == 1:
    classificacao += 1
resposta = int(input('Devia para a vítima? '))
if resposta == 1:
    classificacao += 1  
resposta = int(input('Já trabalhou com a vítima? '))
if resposta == 1:
    classificacao += 1

if classificacao == 2:
    print('Suspeita')
elif classificacao == 3 or classificacao == 4:
    print('Cúmplice')
elif classificacao == 5:
    print('Assassina')
else:
    print('Indeterminado') #só para o programa não responder nada caso o usuário digite outros valores que não contemplem a condição