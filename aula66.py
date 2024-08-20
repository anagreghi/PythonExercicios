"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
Argumento "Posicional" que não tem nome 
"""


#Definição
def soma(x, y, z):
    #print(f'A soma de {x} e {y} é: {x + y}')
    #print(f'A soma de {x = } e {y = } é: {x + y}')
    print(f"{x = } {y = } {z = }", "|", 'x + y + z = ', x + y + z)
    

soma(3, 4, 0)
#soma(4, y=3, 5) #depois de nomear um argumento é necessário nomear os próximos
print(4, 0, 3, sep='-')

