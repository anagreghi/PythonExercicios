"""
REPETIÇÕES
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:

    nome = input('Informe o seu nome: ')
    print(nome)
    if nome == 'sair':
        break