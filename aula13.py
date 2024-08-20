nome = 'Ana Paula'
idade = 30
altura = 1.666
reais = 1298842.99836
peso = 69.589
imc = peso / altura ** 2

#"f-strings"  formatação
linha_1 = f'{nome} tem {idade} anos e {altura:.2f} de altura'
linha_2 = f'{nome} tem {idade} anos e {reais:,.2f} reais'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print('O imc é', linha_3)
print (f'{imc:.2f}')


