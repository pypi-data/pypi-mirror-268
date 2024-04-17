from min_vec.config import MVDB_USER_MESSAGE_PATH


class Authorize:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.authorized = False

    def authorize(self):
        # check username and password if in database
        if self.username == 'admin' and self.password == 'admin':
            self.authorized = True
            return True
        else:
            return False

    def sign_up(self):
        # create new user
        pass
