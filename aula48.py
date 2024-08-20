"""
Listas em Python
Tipo List - Mutável

Suporta vários valores de qualquer tipo
Conhecimentos reuntilizáveis - índices e fatiamento
* Métodos úteis: append, insert, pop, del, clear, extende, +
Create, Read, Update, Delete
"""

#........+012345
#........-54321

string = 'ABCDE' #5 caracteres (len)

#lista = []
#.........0.....1.......2.........3...4
#........-5....-4......-3........-2..-1
lista = [123, True, 'Ana Paula', 1.2, []]
print(lista)
del lista[4]
print(lista)
#print(lista, type(lista))
print(lista[2].upper())
lista[2] = 'Ana Banana'
print(lista[2])
lista[-3] = 'Ana Paula'
print(lista[-3])

#.append(x) -> Adiciona o item ao final da lista
lista_numerica = [10, 20, 30, 40]
print(lista_numerica)
lista_numerica.append(50)
lista_numerica.append(60)
# lista_numerica.pop() #remove o ultimo elemento da lista
ultimo_valor = lista_numerica.pop()
print(lista_numerica, 'Removido o valor:', ultimo_valor)
lista_numerica.append(70)
print(lista_numerica)
