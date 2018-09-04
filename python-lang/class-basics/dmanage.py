import mysql.connector
class DatabaseManager:
    def __init__(self, config):
        self.config = config
        try:
            self.cnx = mysql.connector.connect(**config)
            if self.cnx.is_connected():
                print("\nMySQL server connection successful\n")
                self.cursor = self.cnx.cursor()
                print("Database Cursor Established")
            else:
                print("\nMySQL server not connected\n")
        except mysql.connector.Error as err:
            print("\nSomething went wrong\n")
            print(err)

    def show_tables(self):
        show_tables = "show tables"
        self.cursor.execute(show_tables)
        tables = self.cursor.fetchall()
        print("\nTables in the database\n")
        if tables:
            return [item for item in tables]
        else:
            return []
    # create database creation logic
    def create_database(self, database):
        query = "create database " + str(database).strip()
        try:
            self.cursor.execute(query)
        except(Exception):
            print("Something went wrong")
    # use database
    def use_database(self, database):
        query = "use " + str(database).strip()
        try:
            self.cursor.execute(query)
        except (Exception):
            print("Error in using database " + str(database))
    # show all databases
    def show_databases(self):
        query = "show databases"
        try:
            self.cursor.execute(query)
        except (Exception):
            print("Error in showing databases")
        databases = self.cursor.fetchall()
        return databases


    # create table creating logic with columns
    def create_table(self, table_name, columns):
        # here colums is a dictionay of names as keys and values as types
        types = []
        for key,value in columns.items():
            if value == 'str':
                types.append(key + " " + "varchar(30)")
            if value == 'int':
                types.append(key + " " + "integer")
            if value == 'float':
                types.append(key + " " + "float(8,2)")
        query = "create table " + table_name + " ("
        for i in range(len(columns)):
            query = query + " {},".format(types[i])

        query = query.rstrip(',') + ')'

        #print(query)
        # execute create table query
        try:
            self.cursor.execute(query)
        except (Exception):
            print("Error while creating new table")
        return query
    # create some querying logic

    def select_col(self, column, table):
        sql = "select " + str(column) + " from " + table
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print("\nColumn {0} from table {1}\n".format(column, table))
        for row in rows:
            print(row)
    # select arbitrary number of columns
    def select_cols(self, columns, table):
        # here columns is a list of column names
        sql = "select "
        for i in range(len(columns)):
            sql = sql + columns[i] + ", "
        newsql = sql.strip().rstrip(',') + " from " + str(table)
        #print(newsql)
        # now execute the newsql
        try:
            self.cursor.execute(newsql)
            result = self.cursor.fetchall()
        except (Exception):
            result = [("Somthing went wrong. Possibly due to invalid column names")]
        return result
    def select_all(self, table):
        sql = "select * from " + table
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    def custom_sql(self,query):
        sql = query
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

if __name__ == '__main__':
    config = {"user":"shahid",
              "password": "102mspass",
              "host":"127.0.0.1"
             }

    dm = DatabaseManager(config)
    databases = dm.show_databases()
    #print(databases)
    dm.use_database("tutdb")
    tables = dm.show_tables()
    #print(tables)
    data = dm.select_all("person")
    #print(data)
    dm.select_col("job", "person")
    colss = ["name","salary","sex"]
    res = dm.select_cols(colss, "person")
    print(res)
    #query = dm.create_table("person2", {"name":"str", "age":"int", "salary":"float", "sex":"str"})
