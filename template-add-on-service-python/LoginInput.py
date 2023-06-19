import json


class LoginInput:
    def __init__(self):
        self.username = ""
        self.password = ""

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def __str__(self):
        return "LoginInput [username=" + self.username + ", password=" + self.password + "]"


