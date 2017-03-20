class Username:
    #constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.admin = 0

    def login(self, username, password):
        return self.password == password and self.username == username

    def get_username(self):
        return self.username

    def get_attributes(self):
        return self.username, self.password, self.admin

    def edit_password(self, new_password):
        self.password = new_password

    def get_admin(self):
        return self.admin

class admin(Username):
    #constructor
    def __init__(self, username, password):
        Username.__init__(self, username, password)
        self.admin = 1

    if __name__ == "__main__":