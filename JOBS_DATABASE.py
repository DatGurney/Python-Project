import sqlite3 as SQL

def create_table_jobs(filename = 'customer_database.db'):
    conn = SQL.connect(filename)
    c = conn.cursor()

    #c.execute("DROP TABLE IF EXISTS jobs") #Delete table if it exists
    c.execute("CREATE TABLE IF NOT EXISTS jobs(jobID integer PRIMARY KEY, customerID int, cost decimal, jobDesc text)")

    conn.commit()


def insert_jobs_table(CustomerID, Cost, Description, filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    c.execute("INSERT INTO jobs(customerID, cost, jobDesc) VALUES ('%s','%s','%s')"%(CustomerID, Cost, Description))
    conn.commit()

def print_database(filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    print('Job Data')
    for row in c.execute('SELECT * FROM jobs'):
        print(row)
    print()

    print("User Columns")
    for row in c.execute(("PRAGMA table_info(jobs)")):
        print(row)
    print()

    print("Tables")
    for row in c.execute("SELECT name FROM sqlite_master WHERE type = 'table'"):
        print(row)
    print()

def return_jobs(filename = "customer_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    list = []
    for row in c.execute("SELECT jobID FROM jobs"):
        print(row[0])
        print("hi")
        list.append(row[0])
    return list


if __name__ == "__main__":
    CustomerID, Cost, Description = 1, 200.99, "testing the table"

    create_table_jobs(filename = 'test.db')
    insert_jobs_table(CustomerID, Cost, Description, filename = "test.db")
    print_database(filename="test.db")

    print(return_jobs(filename="test.db"))

    create_table_jobs()




























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