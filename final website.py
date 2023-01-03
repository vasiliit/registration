from string import ascii_letters

class Registration:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

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
        return len(set(c.islower() for c in value if c.isalpha())) == 2

    @staticmethod
    def is_include_only_latin(value):
        return all(c in ascii_letters for c in value if c.isalpha())
    
    @login.setter
    def login(self, new_login):
        if '@' not in new_login:
            raise ValueError("Логин должен содержать один символ '@'")
        if new_login.find('@') > new_login.find('.'):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = new_login

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if not 4 < len(value) < 12:
            raise ValueError("Пароль должен быть длиннее 4 и меньше 12 символов")
        
class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f"ErrorReadFileDeleted({self.name})")
        elif self.in_trash:
            print(f"ErrorReadFileTrashed({self.name})")
        else:
            print(f"Прочитали все содержимое файла {self.name}")

    def write(self, content):
        if self.is_deleted:
            print(f"ErrorWriteFileDeleted({self.name})")
        elif self.in_trash:
            print(f"ErrorWriteFileTrashed({self.name})")
        else:
            print(f"Записали значение {content} в файл {self.name}")

class Trash:
    content = []

    @staticmethod
    def add(file):
        if file.__class__ != File:
            print('В корзину добавлять можно только файл')
        else:
            file.in_trash = True
            Trash.content.append(file)

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for _ in range(len(Trash.content)):
            Trash.content.pop(0).remove()
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for _ in range(len(Trash.content)):
            Trash.content.pop(0).restore_from_trash()
        print('Корзина пуста')

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if self.balance < value:
            print('Не хватает средств на балансе. Пополните счет')
        else:
            self.balance -= value
            return True