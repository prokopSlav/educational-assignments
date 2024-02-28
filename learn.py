"""Задание: написать класс с функциями, проверяющими передаваемые данные с пластиковых карт.
Формат ХХХХ-ХХХХ-ХХХХ-ХХХХ для номера карты и строка с именем и фамилей, разделенной через пробел."""

from string import ascii_lowercase, digits
from typing import List


class CardCheck:
    """Class check card number and name."""

    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str) -> bool:
        numbers: List[str] = number.split('-')
        for count, nums in enumerate(numbers):
            if nums.isdigit() and (len(nums) == 4) and (count < 4):
                continue
            else:
                return False
        if count == 3:
           return True
        return False

    @staticmethod
    def check_name(name: str) -> bool:
        full_name = name.split(' ')
        
        for count, name in enumerate(full_name):
            if (
                name.isalpha()
              and (set(name).issubset(CardCheck.CHARS_FOR_NAME))
              and (count < 2)
            ):
              continue
            else:
              return False
        if count == 1:
            return True
        return False


if __name__ == '__main__':

    is_number = CardCheck.check_card_number("1234-5678-9012-0000")
    is_name = CardCheck.check_name("SERGEI BALAKIREV")
    print(is_number, is_name)


"""Задание: объявить класс Money с проверкой принимаемых значений по условиям(int and >=0)
+ функция сложения значения money из одного объекта класса со значением другого объекта класса."""
class Money:
    def __init__(self, money):
        self.__money = money

    @classmethod
    def __check_money(cls, money):
        if type(money) == int:
            if money >= 0:
                return True
            else:
                return False
        else:
            return False

    def set_money(self, money):
        if self.__check_money(money) is True:
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.__money


"""Задача: реализовать два класса с координатами для создания прямоугольника."""

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, a, b, c=None, d=None):  # Как упростить инициализацию?
        self.__sp = self.__ep = None
        if isinstance(a, Point) and isinstance(b, Point):
            self.__sp = a
            self.__ep = b
        elif all(map(lambda x: type(x) in (int, float), (a, b, c, d))):
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp} {self.__ep}")


rect = Rectangle(0, 0, 20, 34)

assert isinstance(rect, Rectangle) and hasattr(Rectangle, 'set_coords') and hasattr(Rectangle, 'get_coords') and hasattr(Rectangle, 'draw'), "в классе Rectangle присутствуют не все методы"

r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

r = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

assert isinstance(r._Rectangle__sp, Point) and isinstance(r._Rectangle__ep, Point), "атрибуты __sp и __ep должны ссылаться на объекты класса Point"





from random import choices, randint
from string import digits, ascii_letters

"""Задача: реализовать класс для проверки валидности email.
    Условия:
- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.
   Так же необходимо реализовать метод get_random_email для рандомной генерации email."""


class EmailValidator:
    symbol = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._"

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        if isinstance(email, str):
            return True
        else:
            return False

    @classmethod
    def check_email(cls, email):

        def check_point(x):
            if '..' in x:
                return False

        if cls.__is_email_str(email) is False:
            return False

        if not set(email).issubset(cls.symbol):
            return False

        if email.count('@') != 1:
            return False

        email = email.split('@')
        if len(email[0]) > 100 or len(email[1]) > 50:
            return False

        if email[1].count('.') < 1:
            return False

        if check_point(email[0]) is False or check_point(email[1]) is False:
            return False

        else:
            return True

    @classmethod
    def get_random_email(cls):
        my_symbol = f"{digits}{ascii_letters}._"
        email = f"{''.join(choices(my_symbol, k=randint(1, 100)))}@" \
                f"{''.join(choices(my_symbol, k=randint(1, 50)))}.com"
        if cls.check_email(email) is True:
            return email
        else:
            return cls.get_random_email()


"""Тестовый код для наглядного примера, что происходит при создании/обращении к атрибутам объектов класса,
если использовать режимы public, protected(при помощи descriptor) и private(при помощи property)"""


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"{self.name}={value}")
        instance.__dict__[self.name] = value


class Test:

    data = Descriptor()

    def __init__(self, data):
        self.__data = data

    # Для наглядности следующие строки класса советуется закомментировать и посмотреть, что происходит с ними/без них.
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


test = Test('Test')
print(test.__dict__)
test.data = 'Hahaha'
print(test.__dict__)
print('При использовании @property менялся бы атрибут объекта класса с именем _Test__data, а не создавался новый.')
print('Без property:{"_Test__data": "Test", "_data": "Hahaha"}\n')
test.__dict__['data'] = 'data in test'
print(f'Несмотря на внешне одинаковое имя при создании "вручную" атрибута data(222 строка) '
      f'он не изменяет ни атрибуты protected,\nсозданые при помощи descriptor, '
      f'ни атрибуты private(создаваемые при иниализации объекта класса)\n')
test.data = 'Hihihi'
print('Итоговый результат без использования property:\n'
      '{"_Test__data": "Test", "_data": "Hihihi", "data": "data in test"}')
print(f"Итоговый результат при использовании property:\n{test.__dict__}")


"""Задание: реализовать два дескриптора для проверки добавленных товаров в корзину объекта Shop."""
class StringValue:
    def __init__(self, min_length=2, max_length=50, **kwargs):
        self.min_length = kwargs['min_length'] = min_length
        self.max_length = kwargs["max_length"] = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, str) and (self.min_length <= len(value) <= self.max_length):
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value=10000, **kwargs):
        self.max_value = kwargs["max_value"] = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and (0 <= value <= self.max_value):
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)



"""Задача: реализовать класс Product с использованием дандерметодов и валидацией данных внутри них."""

from typing import Union


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 0

    def __new__(cls, *args, **kwargs):
        if cls.id > -1:
            cls.id += 1
        return super().__new__(cls)

    def __init__(self, name: str, weight: Union[int, float], price: Union[int, float]) -> None:
        self.id = self.id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        """Метод валидирует типы входящих значений атрибутов объекта."""
        error_msg = "Неверный тип присваиваемых данных."
        if key == 'name' and not isinstance(value, str):
            raise TypeError(error_msg)

        if key in ('weight', 'price'):
            if not isinstance(value, (int, float)) or value < 0:
                raise TypeError(error_msg)

        self.__dict__[key] = value

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")


"""Задание: сделать систему управления фильтрами. 3 класса с фильтрами для воды, один класс общий блок фильтров.
   Условия для общего блока: 
   1) все фильтры должны быть в строго своих "отсеках
   2) реализовать функцию для старта/стопа воды, которая проверяет наличие всех трех фильтров + их срок службы.
   Условия для фильтров:
   1) Свойства .__date не должны менять при попытке их изменить. Ошибки при попытке изменения генерироваться не должны.""""

import time

class Mechanical:
    def __init__(self, date=None):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = self.__date


class Aragon:
    def __init__(self, date=None):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = self.__date


class Calcium:
    def __init__(self, date=None):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = self.__date


class GeyserClassic:
    MAX_DATE_FILTER = 100
    filters = {1: Mechanical, 2: Aragon, 3: Calcium}
    result = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if self.filters[slot_num] == filter.__class__ and self.result[slot_num] is None:
            self.result[slot_num] = filter

    def remove_filter(self, slot_num):
        self.result[slot_num] = None

    def get_filters(self):
        return self.result[1], self.result[2], self.result[3]  # Как упростить?

    def check_date(self):  # Да простят меня Боги за этот гавнокод...
        _ = []
        if all(self.get_filters()):
            for i in range(1, len(self.result) + 1):
                if 0 <= (time.time() - self.result[i].date) <= 100:
                    _.append(True)
                else:
                    _.append(False)
        if all(_):
            return True
        return False

    def water_on(self):
        if all(self.get_filters()) and self.check_date():
            return True
        return False
