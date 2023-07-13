#Bibliotecas
import pyodbc
import numpy as np



#Funções
def contagemParadas(itens):
    print(len(itens),"x",len(itens[0]))

def conecta_ao_banco(driver='SQL Server', server='PEDRO-PC\SQLPEDRO', database='Duraplast_MES', username=None, password=None, trusted_connection='yes'):

    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor