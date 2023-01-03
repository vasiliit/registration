class Registration:
    def __init__(self, login):
        self.login = login

    @property
    def login(self):
        return self.__login
