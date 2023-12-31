import pyodbc
import numpy as np

def contagemParadas(itens):
    print(len(itens),"x",len(itens[0]))

def conecta_ao_banco(driver='SQL Server', server='PEDRO-PC\SQLPEDRO', database='Duraplast_MES', username=None, password=None, trusted_connection='yes'):

    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor

conexao, cursor = conecta_ao_banco()

itens = cursor.execute('SELECT ClientGroup.Name, Resource.Name, EventDetail.Description,EventType.Description, ServerTimestamp, Event.EventTypeID FROM Event INNER JOIN Resource ON Event.OperatorID = Resource.ResourceID INNER JOIN ClientGroup ON Event.ResourceID = ClientGroup.ClientGroupID INNER JOIN EventType ON Event.EventTypeID = EventType.EventTypeID INNER JOIN EventDetail ON Event.EventDetailID = EventDetail.EventDetailID WHERE (Event.EventTypeID = 8 or Event.EventTypeID = 16) ORDER BY ServerTimestamp;').fetchall()

contagemParadas(itens)





