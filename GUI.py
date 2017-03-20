from tkinter import *
from tkinter import messagebox
import guess_my_password as gmp
import CUSTOMER_DATABASE as CDB

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

        self.menu2_button = Button(self.menu, text="New User", command = new_entry)
        self.menu2_button.grid(row = 2, column = 1)

    def quit(self):
        self.menu.destroy()

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

        self.entry.bind('<Return>', self.submit_entries)
        self.ok_button = Button(self.entry, text="Enter", command=self.submit_entries, width=10)
        self.ok_button.grid(row=4, column=1, sticky="WE", padx=2, pady=3)

        self.quit_button = Button(self.entry, text="Quit", command=self.quit, width=10)
        self.quit_button.grid(row=4, column=2, sticky="W")

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

        self.list = Listbox(height = 10, width = 20, selectmode = EXTENDED)
        self.list.grid(row = 0, column = 0)

        self.List = CDB.return_table()

        for i in self.List:
            print(i)

        list.insert(END, self.List)
        self.ok_button = Button(self.entry, text="login", command = self.print_entries, width = 10)
        self.ok_button.grid(row = 3, column = 1, sticky = "WE", padx = 2, pady = 3)
        self.list.insert(END, "bye")

    def print_entries(self):
        self.Selected = self.list.curselection()
        print(self.Selected)
        print(self.list.get(first=self.Selected))


if __name__ == "__main__":
    #root = login_window()
    root = delete_entry()
    mainloop()