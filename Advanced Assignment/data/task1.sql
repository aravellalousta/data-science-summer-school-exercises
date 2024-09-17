USE attrition_employees;

SELECT * FROM employee_attrition
WHERE EmployeeNumber IN (
    SELECT EmployeeNumber
    FROM employee_attrition
    WHERE Attrition = 'Yes'
    AND YearsAtCompany < 10
    AND MonthlyIncome BETWEEN 2000 AND 15000
    AND (JobRole = 'Sales Executive' OR JobRole = 'Research Scientist' OR JobRole = 'Laboratory Technician')
)
AND Age BETWEEN 25 AND 45
AND PerformanceRating >= 3;