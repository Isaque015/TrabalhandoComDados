from sqlalchemy import create_engine, MetaData
import urllib

conn_str = (
    r'Driver=ODBC Driver 17 for SQL Server;'
    r'Server=localhost;'
    r'Database=python;'
    r'UID=SA;'
    r'PWD=Kl#1j123456;'
)
quoted_conn_str = urllib.parse.quote_plus(conn_str)
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted_conn_str))


metadata = MetaData(bind=engine)
conecta = engine.connect()
