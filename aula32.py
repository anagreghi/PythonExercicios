"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# numero = input('Informe um número inteiro: ')

# if  (numero.isdigit() is False):
#     print('O número não é inteiro')    
# else:
#     numero_inteiro = int(numero)
#     if (numero_inteiro % 2 == 0) :
#         print('O numero é par')
#     else:
#         print('O número não é par')


# entrada = input('Digite um número: ')
# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')





# hora = input('Informe a hora: ')
# hora_inteiro = int(hora)
# if hora_inteiro >= 0 and hora_inteiro < 12:
#     print('Bom dia')
# elif hora_inteiro >= 12 and hora_inteiro < 18:
#     print('Boa tarde')
# elif hora_inteiro >= 18 and hora_inteiro < 24:
#     print('Boa noite')
# else: 
#     print('As horas variam de 00 - 23:59')

entrada = input('Informe um número inteiro: ')
try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')



nome = input('Informe o seu primeiro nome: ')
print(f'Seu nome tem {len(nome)} letras')
comprimento = len(nome)
if comprimento <= 4:
    print('Seu nome é curto')
elif comprimento >= 5 and comprimento <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')


# nome = input('Digite seu nome: ')
# tamanho_nome = len(nome)

# if tamanho_nome > 1:
#     if tamanho_nome <= 4:
#         print('Seu nome é curto')
#     elif tamanho_nome >= 5 and tamanho_nome <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# else:
#     print('Digite mais de uma letra.')