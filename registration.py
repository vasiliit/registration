class Registration:
    def __init__(self, login):
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        if '@' not in new_login:
            raise ValueError("Логин должен содержать один символ '@'")
        if new_login.find('@') > new_login.find('.'):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = new_login