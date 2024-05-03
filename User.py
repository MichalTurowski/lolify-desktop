class User:
    def __init__(self, email, password, name=None):
        self.email = email
        self.password = password
        self.name = name
        self.access_token = None

    def set_access_token(self, token):
        self.access_token = token

    def get_access_token(self):
        return self.access_token
