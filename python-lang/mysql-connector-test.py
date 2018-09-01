import mysql.connector
# the connect() constructor creates a connection to the mysql server
config = {'user':'shahid',
          'password':'102mspass',
          'host':'127.0.0.1',
          'database': 'tutdb'}
try:
    cnx = mysql.connector.connect(**config)
    if cnx.is_connected():
        print("DATABASE CONNECTED")
        cursor = cnx.cursor()
        sql = "select * from person"
        cursor.execute()
    else:
        print("DATABASE NOT CONNECTED")
except mysql.connector.Error as err:
    print(err)
finally:
    cnx.close()
    print("DATABASE CLOSED")


