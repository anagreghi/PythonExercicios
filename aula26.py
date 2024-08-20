"""
Formatação básica de strings
 s - string
 d - int
 f - float
 .<numero de digitos> f
 x ou X - Hexadecimal
 (Caractere)(><^)(quantidade)
 ^ - centro
 > - esquerda
 < - direita
 = - força o número a aparecer antes dos zeros
 sinal - + ou -
 Ex: 0>-100,.1f
 Conversion flags - !r !s !a

 """

variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:$^10}.')
print(f'{1000.028736354553627822:+,.1f}.')
print(f'{1000.028736354553627822:0=+10,.1f}.')