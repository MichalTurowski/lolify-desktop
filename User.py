class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.access_token = None

    def set_access_token(self, token):
        self.access_token = token

    def get_access_token(self):
        return self.access_token
