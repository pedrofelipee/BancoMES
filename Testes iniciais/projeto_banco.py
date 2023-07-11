import pyodbc

def conecta_ao_banco(driver='SQL Server', server='PEDRO-PC\SQLPEDRO', database='master', username=None, password=None, trusted_connection='yes'):

    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor

conexao, cursor = conecta_ao_banco()

itens = cursor.execute('Select * from usuario').fetchall()

print(itens)