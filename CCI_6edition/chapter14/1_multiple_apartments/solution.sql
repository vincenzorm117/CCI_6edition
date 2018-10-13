SELECT tenantname
FROM tenants t
INNER JOIN (
    SELECT tenantid, count(tenantid) cnt
    FROM tenantapartments
    GROUP BY tenantid
    WHERE count(*) > 1
) x
ON x.tenantid = t.tenantid
