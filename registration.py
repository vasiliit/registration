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

    @staticmethod
    def is_include_digit(value):
        return any(char.isdigit() for char in value)

    @staticmethod
    def is_include_all_register(value):
        return len(set(ch.islower() for ch in value if ch.isalpha())) == 2
    
    @staticmethod
    def is_include_only_latin(value):
        return all(ch in ascii_letters for ch in value if ch.isalpha())
    
    @staticmethod
    def check_password_dictionary(value):
        with open('easy_passwords.txt', 'r', encoding='utf-8') as f:
            return value in f.read().split()

    @login.setter
    def login(self, new_login):
        if '@' not in new_login:
            raise ValueError("Логин должен содержать один символ '@'")
        if new_login.find('@') > new_login.find('.'):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = new_login