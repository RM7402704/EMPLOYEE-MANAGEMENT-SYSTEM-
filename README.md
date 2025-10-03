# 💼 Employee Management System (Python + MySQL)

A **Database-driven Employee Management System** built with **Python** and **MySQL** that allows organizations to manage employee information efficiently. The system provides features to **add, remove, promote, and display employee records**, making HR tasks automated, organized, and error-free.

---

## 🛠️ Features

- **Add Employee:** Store employee details (ID, Name, Position, Salary) in the database.  
- **Remove Employee:** Delete employee records securely.  
- **Promote Employee:** Update employee position and salary.  
- **Display Employees:** View all employee details in a clean tabular format.  
- **Database Integration:** All operations are **persistent** and stored in MySQL.  

---

## 📂 Tech Stack

- **Language:** Python 3.x  
- **Database:** MySQL  
- **Libraries & Tools:**  
  - `mysql-connector-python` → Connect Python with MySQL  
  - `tabulate` → Display data in formatted tables  
  - `getpass` → Secure password handling  
- **Optional Tools:** Pandas (for advanced data operations), OS, Regex  

---

## 💻 Installation & Setup

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/RM7402704/employee-management-system.git
   cd employee-management-system



## Note :
Install dependencies:
pip install mysql-connector-python tabulate

**Set up MySQL database:**

CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE employees (
    emp_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    position VARCHAR(50),
    salary FLOAT
);

**Update Database Connection in Python Script:**

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_db"
)

## 📌 How to Use

Add Employee → Input ID, Name, Position, Salary → Employee saved in MySQL.

Remove Employee → Input Employee ID → Record deleted from database.

Promote Employee → Input Employee ID → Update position & salary.

Display Employees → Lists all employee data in a clean table format.


## Project Structure :
employee-management-system/
│
├── employee_management_system.py   # Main Python script
├── README.md                       # Project documentation
├── requirements.txt                # Optional: List of dependencies
└── database_setup.sql              # SQL script to create database & table

