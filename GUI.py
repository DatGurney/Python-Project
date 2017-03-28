from tkinter import *
from tkinter import messagebox
import guess_my_password as gmp
import CUSTOMER_DATABASE as CDB
import TIME_DATABASE as TDB
import JOBS_DATABASE as JDB

class login_window:
    def __init__(self):
        self.window = Tk()
        self.create_widgets()

    def create_widgets(self):
        self.window.geometry("250x70")

        self.window.title("Login")
        #self.output = Text(self.window, width = 20, height = 2, wrap = WORD, background = "white", foreground = "red")
        #self.output.grid(row = 0, column = 2, sticky = W)

        self.username_label = Label(self.window, text = "Username")
        self.username_label.grid(row = 1, column = 1)

        self.username_entry = Entry(self.window, width = 25)
        self.username_entry.grid(row = 1, column = 2)

        self.password_label = Label(self.window, text = "Password")
        self.password_label.grid(row = 2, column = 1)

        self.password_entry = Entry(self.window, width = 25, show = "*")
        self.password_entry.grid(row = 2, column = 2)

        self.ok_button = Button(self.window, text="login", command = self.print_entries, width = 10)
        self.ok_button.grid(row = 3, column = 1, sticky = "WE", padx = 2, pady = 3)

        self.quit_button = Button(self.window, text="quit", command = self.quit, width = 10)
        self.quit_button.grid(row = 3, column = 2, sticky = "W")

    def print_entries(self):
        information = []
        logins = []
        logins = gmp.load_logins(logins)
        print(self.username_entry.get(), self.password_entry.get())
        information.append(self.username_entry.get())
        information.append(self.password_entry.get())
        if gmp.login(logins, information) == information[0]:
            main_window()
            self.quit()
        else: print("Nope")

    def get_user_info(self):
        return self.username_entry.get(), self.password_entry.get()

    def quit(self):
        self.window.destroy()

class main_window:
    def __init__(self):
        self.menu = Tk()
        self.createWidgets()

    def createWidgets(self):
        self.menu.title("Menu")
        self.menu.geometry("800x600")

        self.info_menu_label = Label(self.menu)
        self.info_menu_label.grid(row=0, column = 1)

        self.menu1_label = Label(self.menu, text = "Option 1")
        self.menu1_label.grid(row=1, column=1)

        self.menu1_button = Button(self.menu, text="Exit", command = self.quit)
        self.menu1_button.grid(row = 2, column = 0)

        self.menu1_button2 = Button(self.menu, text="New Client", command = new_entry)
        self.menu1_button2.grid(row = 2, column = 1)

        self.info_menu_label2 = Label(self.menu, text="Option 2")
        self.info_menu_label2.grid(row = 3, column = 1)

        self.menu2_button = Button(self.menu, text = "New User")
        self.menu2_button.grid(row = 4, column = 1)

        self.menu3_button = Button(self.menu, text = "Add Time", command = self.open_time)
        self.menu3_button.grid(row = 5, column = 1)

        self.jobs_list = Listbox(self.menu,height = 20, width = 75, selectmode = EXTENDED)
        self.jobs_list.grid(row = 6, column = 2)

        self.menu1_button3 = Button(self.menu, text="Delete Job", command = delete_entry)
        self.menu1_button3.grid(row = 7, column = 1)

        self.List = CDB.return_table()

        for i in self.List:
            print(i)
            self.jobs_list.insert(END, i)

        self.ok_button = Button(self.menu, text="login", width = 10)
        self.ok_button.grid(row = 3, column = 1, sticky = "WE", padx = 2, pady = 3)
        self.jobs_list.insert(END)

    def quit(self):
        self.menu.destroy()

    def open_time(self):
        add_time()

class new_entry:
    def __init__(self):
        self.entry = Tk()
        self.createWidgets()

    def createWidgets(self):
        self.entry.title("Entry")
        self.phone_label = Label(self.entry, text="Phone")
        self.phone_label.grid(row=1, column=1)

        self.phone_entry = Entry(self.entry, width=25)
        self.phone_entry.grid(row=1, column=2, padx = 40)

        self.client_label = Label(self.entry, text="Client")
        self.client_label.grid(row=2, column=1)

        self.client_entry = Entry(self.entry, width=25)
        self.client_entry.grid(row=2, column=2)

        self.address_label = Label(self.entry, text="Address")
        self.address_label.grid(row=3, column=1)

        self.address_entry = Entry(self.entry, width=25)
        self.address_entry.grid(row=3, column=2)

        self.jobDesc_label = Label(self.entry, text="Job Description")
        self.jobDesc_label.grid(row=4, column=1)

        self.jobDesc_entry = Entry(self.entry, width=25)
        self.jobDesc_entry.grid(row=4, column=2)

        self.entry.bind('<Return>', self.submit_entries)
        self.ok_button = Button(self.entry, text="Enter", command=self.submit_entries, width=10)
        self.ok_button.grid(row=7, column=1, sticky="WE", padx=2, pady=3)

        self.quit_button = Button(self.entry, text="Quit", command=self.quit, width=10)
        self.quit_button.grid(row=7, column=2, sticky="W")

    def quit(self):
        self.entry.destroy()

    def submit_entries(self, *args):
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        client = self.client_entry.get()

        print(address,phone,client)
        if phone.isdigit() and address != "" and client != "":
            CDB.insert_customers_table(client, phone, address)
            CDB.print_database()
            self.quit()
        elif (not phone.isdigit()) or phone == "":
            messagebox.showinfo("Invalid","Phone Number is Invalid")
        elif client == "":
            messagebox.showinfo("Invalid", "Client is Invalid")
        elif address == "":
            messagebox.showinfo("Invalid", "Address is Invalid")

        #self.quit()

class delete_entry:
    def __init__(self):
        self.entry = Tk()
        self.createWidgets()

    def createWidgets(self):
        self.entry.title("Delete Entry")
        self.entry.geometry("800x400")

        self.list = Listbox(height = 10, width = 75, selectmode = EXTENDED)
        self.list.grid(row = 0, column = 0)

        self.List = JDB.return_jobs()

        for i in self.List:
            print(i)
            self.list.insert(END, i)

        self.ok_button = Button(self.entry, text="login", command = self.print_entries, width = 10)
        self.ok_button.grid(row = 3, column = 1, sticky = "WE", padx = 2, pady = 3)
        self.list.insert(END, "bye")

    def print_entries(self):
        self.Selected = self.list.curselection()
        job = self.list.get(first=self.Selected)
        print(job[0])
        JDB.delete_entry(job[0])
        self.entry.destroy()

class add_time:
    def __init__(self):
        self.entry = Tk()
        self.createWidgets()

    def createWidgets(self):
        self.entry.title("Add time to job")

        self.time_label = Label(self.entry, text="Add Hours")
        self.time_label.grid(row=1, column=1)

        self.time_entry = Entry(self.entry, width=25)
        self.time_entry.grid(row=1, column=2, padx = 40)

        self.ok_button = Button(self.entry, text="Enter", command=self.submit_time, width=10)
        self.ok_button.grid(row=7, column=1, sticky="WE", padx=2, pady=3)

        self.list = Listbox(height = 10, width = 20, selectmode = EXTENDED)
        self.list.grid(row = 0, column = 0)

        self.List = CDB.return_table()

        for i in self.List:
            print(i)
            self.list.insert(END, i)

        self.ok_button = Button(self.entry, text="login", command = self.print_entries, width = 10)
        self.ok_button.grid(row = 3, column = 1, sticky = "WE", padx = 2, pady = 3)
        self.list.insert(END, "bye")

    def submit_time(self):
        self.time_entry.get()

class show_customer:
    def __init__(self):
        self.customer = Tk()
        self.createWidgets()

    def createWidgets(self):
        self.customer.title("Delete Entry")
        self.customer.geometry("800x400")

        self.list = Listbox(height = 10, width = 75, selectmode = EXTENDED)
        self.list.grid(row = 0, column = 0)

        self.client_label = Label(self.customer,text = "Client")
        self.client_label.grid(row = 1, column = 1)

        self.client_entry = Entry(self.customer, width=25)
        self.client_entry.grid(row=1, column=2, padx = 40)

    def show_user(self, client):
        self.List = CDB.customer_jobs("John")

        for i in self.List:
            print(i)
            self.list.insert(END, i)

        self.ok_button = Button(self.customer, text="login", width = 10)
        self.ok_button.grid(row = 3, column = 1, sticky = "WE", padx = 2, pady = 3)
        self.list.insert(END, "bye")


if __name__ == "__main__":
    #root = login_window()
    #root = delete_entry()
    root = show_customer()
    mainloop()