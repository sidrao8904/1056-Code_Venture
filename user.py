"""
Definition for the User class.
"""

# Import statements

# User class definition

class User():

    def __init__(self,
                 first_name,
                 last_name,
                 email, 
                 password, 
                 username, 
                 user_id):
    
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.username = username
        self.user_id = user_id

    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getLoginStatus(self):
        return self.login_status
    def setusername(self, username):
        self.username = username
    def setpassword(self, password):
        self.password = password
    def VerifyLogin(self, username, password):

    # Might need to change the definition of this function to get the info 
    # from a database
        if self.username == username and self.password == password:
            self.login_status = True
        else:
            self.login_status = False

    