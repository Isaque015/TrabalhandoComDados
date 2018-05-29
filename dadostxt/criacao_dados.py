# -*- coding: utf-8 -*-
from random import shuffle, randint, uniform, choice
import sys

if sys.stdin.isatty():
    arquivo = open('Nomes.txt', 'r')
else:
    arquivo = open('dadostxt/Nomes.txt', 'r')


nomes = []

for linha in arquivo:
    if str(linha) != '':
        nomes.append(linha.rstrip())

shuffle(nomes)

lista_email = ['@gmail.com', '@outlook.com','@uol.com', '@yahoo.com']

dados = []

for ind in range(50):

    idade = randint(12, 98)
    salario = round(uniform(1000.0, 10000.0), 2)
    email = choice(lista_email)

    item = {'nome':nomes[ind], 'idade': idade, 'email':nomes[ind]+email, 'salario': salario}
    dados.append(item)
