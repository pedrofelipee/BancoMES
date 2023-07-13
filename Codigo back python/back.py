from myfunctions import *


conexao, cursor = conecta_ao_banco()

itens = cursor.execute('SELECT ClientGroup.Name, Resource.Name, EventDetail.Description,EventType.Description, ServerTimestamp, Event.EventTypeID FROM Event INNER JOIN Resource ON Event.OperatorID = Resource.ResourceID INNER JOIN ClientGroup ON Event.ResourceID = ClientGroup.ClientGroupID INNER JOIN EventType ON Event.EventTypeID = EventType.EventTypeID INNER JOIN EventDetail ON Event.EventDetailID = EventDetail.EventDetailID WHERE (Event.EventTypeID = 8 or Event.EventTypeID = 16) ORDER BY ServerTimestamp;').fetchall()

contagemParadas(itens)





