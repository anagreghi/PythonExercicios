"""
Determinada empresa resolveu dar um aumento de salário aos seus colaboradores e 
lhe contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador. Os critérios para reajuste são:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5%
    Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

print('Calculadora de reajuste de salário')
salario = float(input('Informe o salario do colaborador: '))

if salario <= 280:
    aumento = salario * 0.2
    percentual = 20
elif salario > 280 and salario <= 700: 
    aumento = salario * 0.15
    percentual = 15
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.1
    percentual = 10
elif salario > 1500:
    aumento = salario * 0.05
    percentual = 5
else: 
    print('Valor de salário incorreto')

print(f'O salário antes do reajuste é: {salario}')
print(f'O percentual de aumento aplicado foi de {percentual}%')
print(f'O valor do aumento foi de R${aumento}')
print(f'O novo salário após o reajuste é de: R${aumento + salario}')