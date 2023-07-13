/*
SELECT * FROM StatusData

SELECT EventTypeID, OperatorID, UtcTimestamp, EventDetailID FROM Event WHERE EventTypeID = 8;
Select * FROM EventDetail

Select * FROM Client
Select * FROM ClientGroup
SELECT * FROM Resource

SELECT EventTypeID, OperatorID, ServerTimestamp, EventDetailID, Name
FROM Event, ClientGroup, Resource
WHERE (EventTypeID = 16 or EventTypeID = 8) and ClientID = ClientGroupID
ORDER BY ServerTimestamp;

resourceid productionid operatorid

SELECT ClientGroup.Name, Resource.Name, EventDetail.Description,EventType.Description , ServerTimestamp
FROM Event, ClientGroup, Resource, EventDetail, EventType
WHERE (Event.EventTypeID = 16 or Event.EventTypeID = 8) and ClientID = ClientGroupID and Event.OperatorID = Resource.ResourceID
	and Event.EventdetailID = EventDetail.EventdetailID and EventType.EventTypeID = Event.EventTypeID
ORDER BY ServerTimestamp;
*/

SELECT ClientGroup.Name, Resource.Name, EventDetail.Description,EventType.Description , ServerTimestamp, Event.EventTypeID
FROM Event
INNER JOIN Resource ON Event.OperatorID = Resource.ResourceID
INNER JOIN ClientGroup ON Event.ResourceID = ClientGroup.ClientGroupID
INNER JOIN EventType ON Event.EventTypeID = EventType.EventTypeID
INNER JOIN EventDetail ON Event.EventDetailID = EventDetail.EventDetailID
WHERE (Event.EventTypeID = 8 or Event.EventTypeID = 16)
ORDER BY ServerTimestamp;