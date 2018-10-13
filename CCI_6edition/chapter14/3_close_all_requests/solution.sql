UPDATE Requests
SET Status
VALUES ('Closed')
WHERE AptID in (
    SELECT AptID
    FROM Apartments
    INNER JOIN Buildings
    ON Apartments.BuildingID = Buildings.BuildingID
    WHERE BuildingID = 11
)
