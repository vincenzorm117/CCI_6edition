SELECT buildingName, isnull(Cnt, 0)
FROM buildings b
LEFT JOIN (
    SELECT a.buildingid, count(r.requestid) Cnt
    FROM requests r
    INNER JOIN apartments a
    ON r.qptid = a.aptid
    WHERE r.status = ‘Open’
    GROUP BY a.buildingid
) t ON t.buildingid = b.buildingid
