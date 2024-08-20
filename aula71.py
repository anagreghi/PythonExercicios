"""
args - Argumentos não nomeados
*.-.* args (empacotamento e desempacotamento)

"""

#Lembre-te de desempacotamento


x, y, *resto = 1, 2, 3, 4, 5
#x está recebendo 1, y recebe 2 e *resto recebe 3, 4, 5 ... assim por diante
# x e y: desempacotamento
# *resto empacotamento
print(x, y, resto)

# def soma(x, y):
#     print(type(x))
#     return x + y

print(1, 2, 3, 4, 5, 6, 7, 8)

# soma(x, y)


# def soma(*args):
#     print(args, type(args))
#args aqui é uma tupla pq está enviando os dados por um parenteses soma(1, 2, 3, 4, 5)

def soma(*args):
    total = 0
    
    for numero in args:        
        total = total + numero
    return(total)
   # args = list(args)
   
    #args aqui agora é uma lista
soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

print(sum(soma_1_2_3, soma_4_5_6))