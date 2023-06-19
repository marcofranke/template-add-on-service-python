class GetUserInput:
    def __init__(self):
        self.username = ""

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def __str__(self):
        return "GetUserInput [username=" + self.username + "]"