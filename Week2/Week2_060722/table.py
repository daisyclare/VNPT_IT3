import sqlite3 
   
connection = sqlite3.connect("myTable.db") # connecting to the database 
crsr = connection.cursor() # cursor  
  
# SQL command to create a table in the database 
sql_command = """CREATE TABLE IF NOT EXISTS emp (  
    staff_number INTEGER PRIMARY KEY,  
    fname VARCHAR(20),  
    lname VARCHAR(30),  
    gender CHAR(1),  
    joining DATE)"""

crsr.execute(sql_command) # execute the statement
# SQL command to insert the data in the table 
sql_command = """INSERT OR IGNORE INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command) 

# another SQL command to insert the data in the table 
sql_command = """INSERT OR IGNORE INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command) 

# save the changes in the files
connection.commit() 

# close the connection 
connection.close() 