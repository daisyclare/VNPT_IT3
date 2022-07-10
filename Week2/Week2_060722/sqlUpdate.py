import sqlite3 

conn = sqlite3.connect('mydatabase.db') # database name to be passed as parameter 
# update the student record 
conn.execute("UPDATE Student SET name = 'Sam' where unix='B113059'") 
conn.commit() 

print ("Total number of rows updated :", conn.total_changes)
  
cursor = conn.execute("SELECT * FROM Student") 
for row in cursor: 
   print(row) 
  
conn.close() 