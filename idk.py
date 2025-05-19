import sqlite3
conn = sqlite3.connect('students.db')
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (1, 'John', '001', 'Bangalore', '10th')")
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (2, 'Naren', '002', 'Hyd', '12th')")
conn.commit()
conn.close()

query = ('INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) '
         'VALUES (:ID, :NAME, :ROLL, :ADDRESS, :CLASS);')
params = {
        'ID': 3,
        'NAME': 'Jax',
        'ROLL': '003',
        'ADDRESS': 'Delhi',
        'CLASS': '9th'
    }
conn.execute(query, params)

import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.execute("SELECT * from STUDENT")
print(cursor.fetchall())
conn.close()

import sqlite3
conn = sqlite3.connect('students.db')
conn.execute("UPDATE STUDENT set ROLL = 005 where ID = 1")
conn.commit()
cursor = conn.execute("SELECT * from STUDENT")
print(cursor.fetchall())
conn.close()


import sqlite3
conn = sqlite3.connect('students.db')
conn.execute("DELETE from STUDENT where ID = 2;")
conn.commit()
cursor = conn.execute("SELECT * from STUDENT")
print(cursor.fetchall())
conn.close()
