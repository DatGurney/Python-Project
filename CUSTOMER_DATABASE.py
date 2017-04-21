import sqlite3 as SQL

def create_table_customer(filename = 'customer_database.db'):
    conn = SQL.connect(filename)
    c = conn.cursor()

    #c.execute("DROP TABLE IF EXISTS customers") #Delete table if it exists
    c.execute("CREATE TABLE IF NOT EXISTS customers(CustomerID integer PRIMARY KEY, Name text, Phone_Number text, Address text)")

def insert_customers_table(client, phone, address, filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('%s', '%s', '%s')"%(client, phone, address))
    conn.commit()

def load_customers(Customers, filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    SQL_select = "SELECT Name, Phone_Number, Address FROM customers"

    for row in c.execute(SQL_select):
        Customers.append([row[0],row[1],row[2],row[3]])

    conn.commit()

def return_table(filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    list = []
    for row in c.execute("SELECT * FROM customers"):
        print(row)
        list.append(row)
    return list

def print_database(filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    print('Customer Data')
    for row in c.execute('SELECT * FROM customers'):
        print(row)
    print()

    print("User Columns")
    for row in c.execute(("PRAGMA table_info(customers)")):
        print(row)
    print()

    print("Tables")
    for row in c.execute("SELECT Name FROM sqlite_master WHERE type = 'table'"):
        print(row)
    print()

def customer_id(name,filename = 'customer_database.db'):
    conn = SQL.connect(filename)
    c = conn.cursor()

    for row in c.execute("SELECT CustomerID FROM customers WHERE Name = '%s'"%(name)):
        print(row)

#def job_query(CustomerID, filename = 'customer_database.db'):
#    conn = SQL.connect(filename)
#    c = conn.cursor()
#    #Move to gui
#    SQL = "SELECT Customers.CustomerID, Customers.Name, Jobs.JobDesc "
#    SQL = SQL + "FROM Customers INNER JOIN Jobs ON Customers.CustomerID = Jobs.CustomerID "
#    SQL = SQL + "WHERE Customers.CustomerID = '%s'"%(CustomerID)
#
#    #for row in c.execute(SQL):
#        #put row onto text area inside GUI
#

def delete_entry(name, filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    c.execute("DELETE FROM customers WHERE Name = '%s'"%(name))

    conn.commit()

def customer_jobs(name, filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()
    result = c.execute("SELECT jobs.jobDesc, jobs.cost, FROM jobs INNER JOIN customers ON jobs.customerID = customers.CustomerID WHERE customers.Name = '%s'" % (name))
    conn.commit()
    print(result,"result")
    return result

if __name__ == "__main__":
    Client, Phone, Address = "John", "01423772291", "4 new row harrogate"
    create_table_customer(filename="test.db")
    insert_customers_table(Client,Phone,Address, filename="test.db")
    print_database(filename="test.db")
    return_table(filename="test.db")
    insert_customers_table(Client,Phone,Address)
    print(return_table())
    #for row in customer_jobs('John'):
    #    print(row,"printing row")

    print("Customer ID")
    customer_id("John")





























"""





def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Users(playerName text, password text)")
    c.execute("INSERT INTO Users VALUES('', )")
    conn.commit()

    conn.close()

def query():
    sql = "SELECT playerName, password FROM Users"

    for row in c.execute(sql):
        name = row[0]
        strength = row[1]
        print("name: ", name, "\nstrength: ", strength)

def view_database(filename = 'usernames.db'):

    conn = SQL.connect(filename)
    c = conn.cursor()
    # print tables within specific database
    print("List of tables within database")
    for row in c.execute('SELECT name FROM sqlite_master WHERE type="table"'):
        print(row)

    print()

    print("\nWhat would you like to view?")
    print("1. Entire Table")
    print("2. Tables within Row")
    print("3. Load Usernames")
    selection = int(input("\nPlease select an option: "))

    if selection == 1:
        table = input("Please enter field: ")
        #print data within specific table
        print("Users Data")
        try:
            for row in c.execute('SELECT * FROM %s' %table):
                print(row)
        except:
            print("No such Table")

    #print tables within a row
    elif selection == 2:
        table = input("Please enter field: ")
        print("User Columns")
        for row in c.execute('PRAGMA table_info(%s)' %table):
            print(row)

    elif selection == 3:
        logins = []
        logins = load_usernames()

    ###USERS AND LOGINS###

def create_database_table(filename = 'usernames.db'):

    conn = SQL.connect(filename)
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS usernames")
    c.execute("CREATE TABLE usernames(username text, password text)")

def insert_logins(logins, filename = 'usernames.db'):
    c = conn.cursor()

    for item in logins:
        c.execute("INSERT INTO usernames VALUES ('%s', '%s')" %(item[0], item[1]))
    conn.commit()

def load_usernames(filename = 'usernames.db'):
    logins = []
    conn = SQL.connect(filename)
    c = conn.cursor()

    print("Users Data")
    for row in c.execute('SELECT * FROM usernames'):
        print(row)
        row = row.rstrip()
        print(row)
        logins.append(row.rstrip())
    print(logins)
    return logins

if __name__ == "__main__":
    query()
    #view_database()
    #create_database_table()

    #print(load_usernames())

    create_database_table()
"""