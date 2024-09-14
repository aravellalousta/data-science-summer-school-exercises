USE employees;
SELECT Employee_Name, EmpID, GenderID, Department, Position, Salary, PerformanceScore, EmpSatisfaction, EmploymentStatus, Absences FROM employees_table
WHERE PerformanceScore IN ("Exceeds", "Fully Meets")
AND EmploymentStatus = "Active"
AND Salary >= 60000
AND EmpSatisfaction >= 4;