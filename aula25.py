# Interpolação básica de strings
# s - string
# d e i - int
# f - floar
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Ana'
preco = 1000.8493494849
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %x' % (15, 15))
print('O hexadecimal de %d é %04X' % (15, 15))