import sqlite3 as SQL

if __name__ == "__main__":
 conn = SQL.connect("customer_database.db")
 c = conn.cursor()
 c.execute("DROP TABLE IF EXISTS customers")
 c.execute("CREATE TABLE customers(CustomerID integer PRIMARY KEY, Name text, Phone_Number text, Address text)")

 c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('Dan Gurney','07711865025','4 New Row Birstwith')")
 c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('Joshua Hollick','07653245938','3 Kings Road Harrogate')")
 c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('Sam Canham','07635425415','4 Kings Road Harrogate')")
 c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('Harry Merkel','07625736373','25 Finden Gardens Hampswaite')")
 c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('Jamie Leggit','07654897129','21 Spring Road Harrogate')")
 c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('James Gurney','07848766534','4 New Row Birstwith')")
 c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('Judith Gurney','07858630030','4 New Row Birstwith')")
 c.execute("INSERT INTO customers (Name, Phone_Number, Address) VALUES ('Jonny Day','07657482826','8 Fountains Bemd Birstwith')")
 conn.commit()

 print("DONE")