-- Denormalization is the process of optimizing a database by changing a database to become less normalized. This usually creates more reduncies, but it increases read speed as there will be less table joins. In a denormalization, one-to-one or one-to-many relationships are used to combine tables. Consider the following table setup:
Students: StudentID, StudentName
Course: CourseID, StudentID, CourseName
-- When denormalizing, Students might be combined with the Courses table to look like this:
Students: StudentID, StudentName
Course: CourseID, StudentID, StudentName, CourseName
-- As you can see updating students, would take more than one query as you have to update them in 2 places, but now you can do one query for courses.
