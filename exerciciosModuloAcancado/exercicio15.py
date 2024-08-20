""" 
Faça um Programa que peça dois números inteiros e imprima a soma. 
Criar funções para manter o código organizado.
"""

def ler():
    numero_1 = int(input('Informe um número: '))
    numero_2 = int(input('Informe outro número: '))
    return numero_1, numero_2
    

def soma(numero_1, numero_2):
    total = numero_1 + numero_2
    return total
    
def main():
    numero_1, numero_2 = ler()
    resultado = soma(numero_1, numero_2)
    print(f'A soma é {resultado}')


if __name__ == "__main__":
    main()