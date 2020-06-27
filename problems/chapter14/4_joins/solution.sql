

-- Joins combine 2 or more tables/results on a matching expression usually by a table id. There are 4 different types of joins: LEFT JOIN, RIGHT JOIN, INNER JOIN, and FULL OUTER JOIN. FULL OUTER JOIN is not supported on all SQL languages, but there are quries that can produce the same idea.

-- Consider the following example for the following explanations:
SELECT Students.StudentName, Courses.CourseName
FROM Students
LEFT JOIN Courses
ON Students.StudentID = Courses.StudentID

-- To clarify what is meant by left and right, in the query above, the left table is the Students table and the right table is the Courses table.

-- LEFT JOIN joins 2 tables, and tries to match everything on the left table with everything on the right. Any left table rows that don't get matched with the right table are still kept in the result, but the same is not the case for the right table. Left table rows that don't have a matching right table row, have NULL entries for the right table row columns. In a RIGHT JOIN, everything is the same except the right table rows are kept and the right might not be.
-- Left joins are beneficial when working with a one-to-many table relationship. Say A has a one-to-many relationship to B. LEFT JOIN helps in getting all the records of B matching or not matching with A.

-- INNER JOIN joins 2 table, but only keeps rows that match in both tables. This is beneficial when you want to exclude items on the left table that don't match with items on the right table.

-- OUTER JOIN joins 2 tables, and keeps all rows from both tables. Its like a LEFT and RIGHT join combined, so that means that there can result in NULL values on either side.
