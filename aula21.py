#Operadores lógicos
# and (e) or (ou) not (não)
#and - todas as condições precisam ser verdadeiras
# 0 0.0 '' False
#none - não valor

#falsy

#if 0 and 1:
#    print(True and 1)

entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else: 
    print('Sair')

