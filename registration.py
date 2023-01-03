from string import ascii_letters

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @login.setter
    def login(self, new_login):
        if '@' not in new_login:
            raise ValueError("Логин должен содержать один символ '@'")
        if new_login.find('@') > new_login.find('.'):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = new_login

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

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if not 4 < len(value) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value