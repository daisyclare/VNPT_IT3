import sqlite3 
  
conn = sqlite3.connect('mydatabase.db')            # database name to be passed as parameter 
  
# delete student record from database 
conn.execute("DELETE from Student where unix='B113058'") 
conn.commit() 

print("Total number of rows deleted :", conn.total_changes)
  
cursor = conn.execute("SELECT * FROM Student") 
for row in cursor: 
   print(row), 
  
conn.close()