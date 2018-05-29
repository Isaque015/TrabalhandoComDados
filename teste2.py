import xlsxwriter as xlsx
from scriptsSGDB.select import cabecalho
from dadostxt.criacao_dados import dados

from os.path import isdir
from os import mkdir


if not isdir('planilhas'):
    mkdir('planilhas')


arquivo = xlsx.Workbook('planilhas/teste.xlsx')
planilha = arquivo.add_worksheet('teste')
bold = arquivo.add_format({'bold': True})
money = arquivo.add_format({'num_format':'$#,00'})

for ind, item in enumerate(cabecalho):
    if item == 'id':
        continue
    planilha.write((ind+1)//(ind+1), ind, item, bold)

ind = 2
for linha, dado in enumerate(dados):
    planilha.write(linha+2, ind-1, dado['nome'])
    planilha.write(linha+2, ind, dado['idade'])
    planilha.write(linha+2, ind+1, dado['email'])
    planilha.write(linha+2, ind+2, dado['salario'], money)
arquivo.close()
