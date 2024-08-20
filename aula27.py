"""
Fatiamento de strings
Fatiamento: [i:f:p] [::]
012345678
-987654321
Função len retorna a qtd de caracteres da str
"""
nome = 'Ana Paula'
variavel = 'Olá mundo'
print(nome[0:])
print(nome[0:3])
print(nome[:3])
print(nome[3:9])

print(len(variavel)) 
print(variavel[0:len(variavel):2])
print(variavel[0:9:2])
print(variavel[::-1])
print(variavel[-1:-10:-2])