# Employee Management System using Python + MySQL
import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

# Connect to Database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="raja123",
    database="employee_db"
)

# Check if employee exists
def check_employee(emp_id):
    try:
        cursor = con.cursor()
        query = "SELECT * FROM employees WHERE id=%s"
        cursor.execute(query, (emp_id,))
        result = cursor.fetchone()
        return result is not None
    except Error as e:
        print(f"Error checking employee: {e}")
    finally:
        cursor.close()
    return False

# Add Employee
def add_employee():
    emp_id = input("Enter Employee Id: ")

    if check_employee(emp_id):
        print("❌ Employee already exists. Please try again.")
        return

    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    salary = input("Enter Employee Salary: ")

    sql = "INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)"
    data = (emp_id, name, position, salary)

    cursor = con.cursor()
    try:
        cursor.execute(sql, data)
        con.commit()
        print("✅ Employee Added Successfully")
    except Error as e:
        print(f"Error adding employee: {e}")
        con.rollback()
    finally:
        cursor.close()

# Remove Employee
def remove_employee():
    emp_id = input("Enter Employee Id to remove: ")
    if not check_employee(emp_id):
        print("❌ Employee does not exist.")
        return
    try:
        cursor = con.cursor()
        query = "DELETE FROM employees WHERE id=%s"
        cursor.execute(query, (emp_id,))
        con.commit()
        print("🗑️ Employee removed successfully.")
    except Error as e:
        print(f"Error removing employee: {e}")
        con.rollback()
    finally:
        cursor.close()

# Promote Employee
def promote_employee():
    emp_id = input("Enter Employee Id to promote: ")
    if not check_employee(emp_id):
        print("❌ Employee does not exist.")
        return

    new_position = input("Enter new position: ")
    new_salary = input("Enter new salary: ")

    try:
        cursor = con.cursor()
        query = "UPDATE employees SET position=%s, salary=%s WHERE id=%s"
        cursor.execute(query, (new_position, new_salary, emp_id))
        con.commit()
        print("📈 Employee promoted successfully.")
    except Error as e:
        print(f"Error promoting employee: {e}")
        con.rollback()
    finally:
        cursor.close()

# Display Employees
def display_employees():
    try:
        cursor = con.cursor()
        query = "SELECT * FROM employees"
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            print(tabulate(rows, headers=["Employee ID", "Name", "Position", "Salary"], tablefmt="grid"))
        else:
            print("No employees found.")
    except Error as e:
        print(f"Error displaying employees: {e}")
    finally:
        cursor.close()

# Menu
def menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Promote Employee")
        print("4. Display Employees")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            remove_employee()
        elif choice == '3':
            promote_employee()
        elif choice == '4':
            display_employees()
        elif choice == '5':
            print("👋 Exiting the system.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
    con.close()
