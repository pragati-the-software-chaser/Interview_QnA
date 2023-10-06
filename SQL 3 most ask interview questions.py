#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install ipython-sql 1)Load the Extension, 2)Check SQL Cell
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite://')
#%reload_ext sql


# Create Employees Table:

# In[2]:


get_ipython().run_cell_magic('sql', '', 'DROP TABLE IF EXISTS Employees;\n\n\nCREATE TABLE Employees (\n    EmployeeID INT ,\n    FirstName VARCHAR(255),\n    LastName VARCHAR(255),\n    Salary INT,\n    CreditDate DATE\n);')


# Insert Sample Data into Employees Table:

# In[3]:


get_ipython().run_cell_magic('sql', '', "INSERT INTO Employees (EmployeeID, FirstName, LastName, Salary, CreditDate)\nVALUES (1, 'John', 'Doe', 50000,'2023-06-01'),\n       (2, 'Alice', 'Smith', 60000,'2023-06-20'),\n       (3, 'Bob', 'Johnson', 55000,'2023-07-01'),\n       (3, 'Bob', 'Johnson', 55000,'2023-07-01'),\n       (5, 'Eva', 'Brown', 65000,'2023-08-01'),\n       (6, 'Mike', 'Wilson', 70000,'2023-08-05');")


# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM Employees;')


# # 1.Find the 3th Highest Salary:

# Using Limit and Offset

# In[10]:


get_ipython().run_cell_magic('sql', '', '\nSELECT DISTINCT Salary\nFROM Employees\nORDER BY Salary DESC\nLIMIT 1 OFFSET 3 - 1;')


# Using ORDER BY

# In[11]:


get_ipython().run_cell_magic('sql', '', '\nSELECT Salary\nFROM Employees\nWHERE Salary IN (SELECT Salary FROM Employees ORDER BY Salary DESC LIMIT 3)\nORDER BY Salary ASC\nLIMIT 1;')


# Using Window function

# In[12]:


get_ipython().run_cell_magic('sql', '', '\nWITH RankedSalaries AS (\n    SELECT Salary, \n           RANK() OVER (ORDER BY Salary DESC) AS RankOfTheSalary\n    FROM Employees\n)\nSELECT Salary\nFROM RankedSalaries\nWHERE RankOfTheSalary = 3;')


# # 2.Find Duplicate Rows:

# In[13]:


get_ipython().run_cell_magic('sql', '', 'SELECT EmployeeID, COUNT(*)\nFROM Employees\nGROUP BY EmployeeID\nHAVING COUNT(*) > 1;')


# In[14]:


# Remove Duplicate Rows:


# %%sql
# 
# DELETE FROM Employees
# WHERE EmployeeID IN (
#     SELECT EmployeeID
#     FROM Employees
#     GROUP BY EmployeeID
#     HAVING COUNT(*) > 1
#     LIMIT 1
# );

# In[17]:


get_ipython().run_cell_magic('sql', '', 'SELECT * \nFROM Employees;')


# # 3.Calculate Cumulative Sum:

# In[11]:


get_ipython().run_cell_magic('sql', '', '\nSELECT EmployeeID, Salary, \n       SUM(Salary) OVER (ORDER BY EmployeeID) AS CumulativeSum\nFROM Employees;')

