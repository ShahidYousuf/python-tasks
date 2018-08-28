import mysql.connector
# the connect() constructor creates a connection to the mysql server
config = {'user':'shahid',
          'password':'102mspass',
          'host':'127.0.0.1',
          'database': 'tutdb'}
try:
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        print("\nDATABASE CONNECTED")
        cursor = cnx.cursor()
        # read from database
        sql = "select * from person"
        cursor.execute(sql)
        row = cursor.fetchone()
        print("\nFetch using cursor.fetchone()")
        print()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        print("\nFetch using cursor.fetchall()")
        print()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        sql1 = "select name, job, sex from person order by name"
        cursor.execute(sql1)
        rows = cursor.fetchall()
        print("\nFetch only selected columns from the database\n")
        for row in rows:
            print(row)
        # trying insert, uncomment to see effect
        # sql2 = "insert into person values ('smith', 'electrician', 1044, 'm')"
       # cursor.execute(sql2)
       # cnx.commit()
        cursor.execute(sql)
        rows = cursor.fetchall() # rows is of type list
        print("\nDatabase after insertion of another row\n")
        for row in rows:
            print(row) # row is of type tuple
    else:
        print("\nDATABASE NOT CONNECTED")
except mysql.connector.Error as err:
    print(err)
finally:
    cnx.close()
    print("\nDATABASE CLOSED")


