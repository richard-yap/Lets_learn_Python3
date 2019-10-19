#-------------------------------DATABASES-------------------------------------
#exploring SQLite
#SQLite is a local file no server
import sqlite3

db = sqlite3.connect("test.db")
#supposed to use a driver to read its content

#this comand will create a table for us, with 2 columns name and rank
db.execute("CREATE TABLE students (name text, rank int)")
#whenever you run the database, you need to do commit to apply change to your harddisk
db.commit()

#Creating and inserting data:
db.execute("INSERT INTO students (name, rank) values (?, ?)", ("A", 1))
db.commit() #whenever you modify yr data base you must commit()

#reading they data:
students = dbexecute("SELECT * FROM students ORDER BY rank")
#dunnid to commit() since u didn't update the database
for s in students:
    #result will be a tuple
    print(s)

#updating the database:
db.execute("UPDATE studemts SET name=? WHERE rank=?", ("B", 1))
db.commit()
