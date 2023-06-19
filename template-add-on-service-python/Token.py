class Token:
    def __init__(self):
        self.token = ""

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def __str__(self):
        return "Token [token=" + self.token + "]"
