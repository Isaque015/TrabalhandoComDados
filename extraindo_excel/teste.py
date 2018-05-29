from os import path
import sys, inspect
import pandas as pd

currentdir = path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = path.dirname(currentdir)
sys.path.insert(0,parentdir)

xlsx = pd.ExcelFile('planilhas/teste.xlsx')
df = pd.read_excel(xlsx, 'testes')

dados_pandas = []

for index, row in df.iterrows():
    dic = {'nome':row['nome'], 'idade':row['idade'], 'email':row['email'], 'salario':row['salario']}
    dados_pandas.append(dic)


for item in dados_pandas:
    print(item)
