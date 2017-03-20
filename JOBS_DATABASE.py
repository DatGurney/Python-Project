import sqlite3 as SQL

def create_table_jobs(filename = 'stack_database.db'):
    conn = SQL.connect(filename)
    c = conn.cursor()

    #c.execute("DROP TABLE IF EXISTS usernames") #Delete table if it exists
    c.execute("CREATE TABLE IF NOT EXISTS jobs(jobID INTEGER PRIMARY KEY, customerID INTEGER,"
              "cost DECIMAL, jobDesc TEXT")



def insert_jobs_table(CustomerID, Cost, Description, filename = "stack_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    for item in Passwords:
        c.execute("INSERT INTO jobs (customerID, cost, jobDesc VALUES ('%s','%s','%s',)"%(item[0], item[1]),)
    conn.commit()

def select_usernames_table(Passwords, filename = "stack_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    SQL_select = "SELECT username, password FROM usernames"

    for row in c.execute(SQL_select):
        Passwords.append([row[0],row[1]])

    conn.commit()

def print_database(filename = "stack_database.db"):
    conn = SQL.connect(filename)
    c = conn.cursor()

    print('Users Data')
    for row in c.execute('SELECT * FROM usernames'):
        print(row)
    print()

    print("User Columns")
    for row in c.execute(("PRAGMA table_info(usernames)")):
        print(row)
    print()

    print("Tables")
    for row in c.execute("SELECT name FROM sqlite_master WHERE type = 'table'"):
        print(row)
    print()

if __name__ == "__main__":
    Passwords = [["DST", "Password1"],["KLN", "Password2"]]
    create_table_jobs(filename = 'test.db')
    insert_jobs_table(Passwords, filename = "test.db")
    print_database(filename="test.db")





























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