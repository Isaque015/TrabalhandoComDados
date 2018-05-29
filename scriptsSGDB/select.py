from .conexao import metadata, conecta, engine
from sqlalchemy import select, Table

teste = Table('teste2', metadata, autoload=True, autoload_with=engine)


select = select([teste])
x = select.execute()
print()

cabecalho = []

for row in select.execute().keys():
    cabecalho.append(row)
