"""
FLAG (Bandeira) - Marcar um local
none = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

#ocupa o mesmo local na memória pq tem o mesmo valor 'a'

condicao = True
passou_no_if = None

if condicao: 
    print('Faça algo')
else: 
    print('Não faça algo')

if (passou_no_if) is None:
    print('Não passou no if')
else:
    print('Passou no if')