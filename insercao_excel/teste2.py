from os.path import isdir
from os import mkdir, path
import sys, inspect
import xlsxwriter as xlsx

currentdir = path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = path.dirname(currentdir)
sys.path.insert(0,parentdir)


from scriptsSGDB.select import cabecalho
from dadostxt.criacao_dados import dados



def escolher_cor_linha(linha):
    if linha % 2 == 0:
        return linha_par
    return linhha_impar

def escolher_cor_money(linha):
    if linha % 2 == 0:
        return money
    return money_impar

if not isdir('planilhas'):
    mkdir('planilhas')


arquivo = xlsx.Workbook('planilhas/teste.xlsx')
planilha = arquivo.add_worksheet('testes')

# ------------ '' FORMATAÇÂO '' -----------------
money_impar = arquivo.add_format({'num_format':'$#,00', 'border':1, 'border_color':'#000000', 'align': 'center', 'bg_color': '#E8F6F9'})
money = arquivo.add_format({'num_format':'$#,00', 'border':1, 'border_color':'#000000', 'bg_color':'#C5E9F0', 'align': 'center'})
bg_cabecalho = arquivo.add_format({'bold':True, 'font_size': 12, 'border':1, 'border_color': "#000000", 'align': 'center' })
linha_par = arquivo.add_format({'bg_color':'#C5E9F0', 'border':1, 'border_color':'#000000', 'align': 'center'})
linhha_impar = arquivo.add_format({'border':1, 'border_color':'#000000', 'align': 'center', 'bg_color': '#E8F6F9'})
# ------------ '' FIM FORMATAÇÂO '' -----------------


for ind, item in enumerate(cabecalho):
    if item == 'id':
        continue
    planilha.write((ind+1)//(ind+1), ind, item, bg_cabecalho)



ind = 2
for linha, dado in enumerate(dados):
    planilha.write(linha+2, ind-1, dado['nome'], escolher_cor_linha(linha))
    planilha.write(linha+2, ind, dado['idade'], escolher_cor_linha(linha))
    planilha.write(linha+2, ind+1, dado['email'], escolher_cor_linha(linha))
    planilha.write(linha+2, ind+2, dado['salario'], escolher_cor_money(linha))


planilha.set_column("B:E", 20)

arquivo.close()
