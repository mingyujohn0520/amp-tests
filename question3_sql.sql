##sql
SELECT E.NAME,
COALESCE(U.UIN,'NULL') AS UIN
FROM EMPLOYEE E 
LEFT JOIN EMPLOYEE_UNIN U ON E.ID =U.ID