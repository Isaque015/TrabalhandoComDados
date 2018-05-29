from sqlalchemy import Table

# ====== // ===========
from .conexao import (engine, metadata, conecta)


user_table = Table('teste2', metadata, autoload=True, autoload_with=engine)

elementos = [
    {'nome':'SelokoMel', 'idade':'88', 'email':'igigig', 'salario':'111111'},
    {'nome':'SelokoMel', 'idade':'88', 'email':'igigig', 'salario':'111111'},
    {'nome':'SelokoMel', 'idade':'88', 'email':'igigig', 'salario':'111111'},
]

for ele in elementos:
    ins = user_table.insert().values(ele)
    conecta.execute(ins)
