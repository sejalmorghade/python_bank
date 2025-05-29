-- Create a stored procedure to insert a new employee record
DELIMITER //
CREATE PROCEDURE InsertEmployee(
IN emp_nameVARCHAR(255),
IN emp_salaryDECIMAL(10, 2),
IN emp_departmentVARCHAR(100)
)
BEGIN
INSERT INTO employees (name, salary, department)
VALUES (emp_name, emp_salary, emp_department);
END //
DELIMITER ;
-- Call the stored procedure to insert a new employee record
CALL InsertEmployee('John Doe', 50000.00, 'IT');
-- Create a stored procedure to update an employee's salary
DELIMITER //
CREATE PROCEDURE UpdateSalary(
IN emp_id INT,
IN new_salaryDECIMAL(10, 2)
)
BEGIN
UPDATE employees
SET salary = new_salary
WHERE id = emp_id;
END //
DELIMITER ;
-- Call the stored procedure to update an employee's salary
CALL UpdateSalary(1, 55000.00);
