# GuessMyPassword.py is a quick revision application.

import os
import LinearSearch as ls
import STACK as sk
import re
import GUI
import DATABASE as db

counter = 0
logins = []
def login(logins, input):
    found = False
    username = input[0]
    password = input[1]
    #username = input("please enter username: ")
    #password = input("please enter password: ")
    for item in logins:
        print(item[0])
        print(item[1])
        if item[0] == username and item[1] == password:
            found = True
            break
    print("you got it")
    return item[0]

def check_for_file():
    print(os.path.dirname(os.path.abspath(__file__)))
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    list_of_files = []
    counter = 1
    for f in files:
        list_of_files.append(f)
    number_of_files = int(len(list_of_files))
    for i in list_of_files:
        print(counter)
        print(i)
        if i == "logins.txt":
            print("Login Data Has been found and Registered")
            break
        elif i != "logins.txt" and counter == number_of_files:
            print("Creating new File. Assuming This is newly loaded or data has been deleted")
            file = open("logins.txt", "w")
            file.close()
            #save_names() change this to your create user function

        else:
            print("did 3")

        counter = counter + 1

def delete_user(logins):
    found = False
    while found == False:
        username = input("please enter username: ")
        password = input("please enter password: ")
        for item in logins:
            print(item[0])
            #print(item[1])
            if item[0] == username and item[1] == password:
                logins.remove(item)
                found = True
                break
    print("you got it")

def load_database_logins(logins):
    db.view_database



def load_logins(logins):
    check_for_file()
    with open('logins.txt', 'r') as file:
        for line in file:
            line = line.split(',')
            logins.append([line[0].rstrip(), line[1].rstrip()])
    return logins

    #db.load_usernames

def save_names():
    username = input("Please enter a username. It must be an email address: ")
    password = input("Please enter a password: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", username):
        username = input("Please enter a username. It mused be an email address: ")
        password = input("Please enter a password: ")

    with open('logins.txt', 'a') as file:
        file.write(username + ',' + password + '\n')

def save_to_file(logins):
    with open('logins.txt', 'a') as file:
        file.write(username + ',' + password + '\n')

def view_stack(last_login,stack):
    stack.print_stack()

def push_login_to_stack(stack,last_login):
    stack.push_stack(last_login)
    print(stack.print_stack())
    return stack

def welcome(logins, last_login,stack):
    print("Hello.\n")
    print("\n")
    print("Please Select an option:")
    print("\n")
    print("1. Login")
    print("2. Create New Account")
    print("3. Search for User; Linear Search")
    print("4. Search for User; Binary Search")
    print("5. Remove User")
    print("6. Stack implementation")
    print("7. View Database")
    print("\n")
    print("8. Exit")

    selection = int(input("Select a number: "))
    exit_code = False
    if selection == 1:
        stack.push_stack(last_login)
        print(stack)
        last_login = login(logins)
    elif selection == 2:
        save_names()
    elif selection == 3:
        search = input("What Name would you like to search for: ")
        ls.LinearSearch(logins, search)
    elif selection == 4:
        search = input("What Name would you like to search for: ")
        ls.binary_search_2d(logins, search)
    elif selection == 5:
        delete_user(logins)
    elif selection == 6:
        latest_stack = view_stack(last_login,stack)
        print(latest_stack)
    elif selection == 7:
        db.view_database()
    elif selection == 8:
        exit_code = True
    return exit_code, last_login, stack

    go_again = input

# Start Main
if __name__ == "__main__":
    stack_size = 100
    stack = sk.stack(stack_size)
    logins = load_logins(logins)
    ls.BubbleSort(logins)
    print(logins)
    last_login = login(logins)
    exit_code = False
    print("HI")
    stack.print_stack()

    while exit_code != True:
        exit_code, last_login, stack = welcome(logins, last_login,stack)
        logins = load_logins(logins)
    print("end")
    save_stack(stack)
    db.create_database_table()
    db.insert_logins(logins)

#SQL Testing Site: http://www.w3schools.com/sql/trysql.asp?filename=trysql_delete