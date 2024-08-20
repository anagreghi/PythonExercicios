# Operadores in e not in
# Strings são iteráveis
# A n a  P a u l a
# 0 1 2 3 4 5 6 7 8
# -9 -8 -7 -6 -5 -4 -3 -2 -1

""" nome = 'Ana Paula'

print(nome[-9], nome[-8])

print('a' in nome)
print('zero' in nome)
print('-' * 10)
print('a' not in nome)
print('zero' not in nome) """

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

    #ATENÇÃO!!! CASESENSITIVE