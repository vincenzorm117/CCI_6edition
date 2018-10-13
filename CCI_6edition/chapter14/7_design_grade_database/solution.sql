
-- TABLES:
-- Students: StudentID INT, StudentName VARCHAR
-- Courses: CourseID* INT, CourseName VARCHAR
-- StudentCourses: StudentID* INT, CouseID* INT, grade INT
-- A-5 points, B-4 points,C-3 points, D-2 points, E-1 point, F-0 points

-- QUERY:
set @index = 0
set @total = (SELECT count(*) FROM Students)

SELECT StudentName, GPA
FROM (
    SELECT S.StudentName StudentName, ISNULL(GPA, 0) AS GPA, @index := @index + 1 AS INDEX
    FROM Students
    LEFT JOIN (
        SELECT StudentID, AVG(grade) GPA
        FROM StudentCourses
        GROUP BY CourseID
    ) T
    ON S.StudentID = T.StudentID
    ORDER BY GPA DESC
)
WHERE (INDEX / @total) < .1;
