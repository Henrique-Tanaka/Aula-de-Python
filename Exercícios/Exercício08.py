"""
Faça um programa que peça para o usuario digitar o nome e aconteça esse exemplo:*H*e*n*r*i*q*u*e*
"""
nome = input('digite seu nome: ')

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
