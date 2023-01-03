from string import ascii_letters

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, new_login):
        if '@' not in new_login:
            raise ValueError("Логин должен содержать один символ '@'")
        if new_login.find('@') > new_login.find('.'):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = new_login