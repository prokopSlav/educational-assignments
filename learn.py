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


class Filter:

    def __init__(self, date=None):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        ...


class Mechanical(Filter):

    ...


class Aragon(Filter):

    ...


class Calcium(Filter):

    ...


class GeyserClassic:
    """Класс управления фильтрами и водой."""

    MAX_DATE_FILTER = 100
    slots = {1: Mechanical, 2: Aragon, 3: Calcium}
    result = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num: int, filter: Filter) -> None:
        """Функция добавления фильтра в гейзер."""
        if self.slots[slot_num] == filter.__class__ and self.result[slot_num] is None:
            self.result[slot_num] = filter

    def remove_filter(self, slot_num: int) -> None:
        """Функция удаления фильтра из гейзера."""
        self.result[slot_num] = None

    def get_filters(self) -> tuple:
        """Полученеи кортежа установленных фильтров."""
        mechanical, aragon, calcium = self.result.values()
        return mechanical, aragon, calcium

    def water_on(self) -> bool:
        """Функция включения воды."""
        for index, value in enumerate(self.get_filters()):
            if not value:
                return False
            if not (0 <= (time.time() - self.result[index+1].date) <= self.MAX_DATE_FILTER):
                return False
        return True




"""Реализация базовой логики игры в сапер без взаимодействия в консоли."""

import copy
import random


class Cell:
    """Класс, определяющий модель каждой клетки игры в Сапёр."""

    def __init__(self) -> None:
        """Создание клетки поля с базовыми параметрами."""
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, mine: bool) -> None:
        if not isinstance(mine, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = mine

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, new_number: int) -> None:
        if not 0 <= new_number <= 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = new_number

    @property
    def is_open(self) -> bool:
        return self.__is_open

    @is_open.setter
    def is_open(self, open: bool) -> None:
        if not isinstance(open, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = open

    def __bool__(self) -> bool:
        """Проверка на открытую или закрытую клетку."""
        return True if self.__is_open is False else False


class GamePole:
    """Класс, моделирующий поведение игрового поля в Сапёр."""
    _instance = None

    def __new__(cls, *args, **kwargs) -> object:
        """Метод для реализации паттерна Singleton."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, N: int, M: int, total_mines: int) -> None:
        """Метод для инициализации игрового поля по паметрам высоты, ширины и количества мин на поле."""
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for i in range(self.M)] for j in range(self.N)]

    @property
    def pole(self) -> list:
        """Получение ссылки на матрицу с игровым полем."""
        return self.__pole_cells

    def init_pole(self) -> None:
        """Функция для старта новой игры.
           Заполнение поля минами и определние количества мин для каждой клетки."""
        _mines = set()
        while len(_mines) < self.total_mines:
            random_cell = random.choice(random.choice(self.__pole_cells))
            random_cell.is_mine = True
            _mines.add(random_cell)
        for i in self.__pole_cells:
            for j in i:
                j.is_open = False
        for index_row, row in enumerate(self.__pole_cells):
            for index_column, column in enumerate(row):
                self.search_mines(index_row, index_column)

    def open_cell(self, x: int, y: int) -> None:
        """Функция, проверяющая корректность индекса выборанной клетки.
        Если клетка существует, она становится открытой."""
        if x >= self.N or y >= self.M:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[x][y].is_open = True
        self.search_mines(x, y)

    def show_pole(self) -> None:
        """Визуальное представление игрового поля в консоли."""
        copy_pole = copy.deepcopy(self.__pole_cells)
        for index_i, i in enumerate(copy_pole):
            for index_j, j in enumerate(i):
                if not j.is_open:
                    copy_pole[index_i][index_j] = '?'
                if j.is_open:
                    copy_pole[index_i][index_j] = j.number
                if j.is_mine:
                    copy_pole[index_i][index_j] = '*'
        for i in copy_pole:
            print(*i)

    def search_mines(self, x: int, y: int) -> None:  # написать свою реализацию через метод скользящего окна
        """Функция поиска мин в радиусе одной клетки от выбранной клетки."""
        count = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                ii, jj = k + y, l + x
                if ii < 0 or ii > self.M-1 or jj < 0 or jj > self.N-1:
                    continue
                if self.__pole_cells[jj][ii].is_mine:
                    count += 1
        self.__pole_cells[x][y].number = count



"""Игра в крестики-нолики."""

class TicTacToe:
    """Класс, моделирующий поведение игрового поля для игры в крестики-нолики."""

    def __init__(self) -> None:
        """Создание игрового поля для игры в крестики-нолики."""
        self.pole = tuple([Cell() for _ in range(3)] for _ in range(3))

    def __getitem__(self, item: tuple) -> any((tuple, int)):
        """Функция для показа значений строк/столбцов или клеток игрового поля."""
        if slice(None) in item:
            if isinstance(item[0], int):
                return tuple(i.value for i in self.pole[item[0]])
            else:
                column = []
                for row in self.pole:
                    column.append(row[item[1]].value)
                return tuple(column)
        else:
            return self.pole[item[0]][item[1]].value

    def __setitem__(self, key: tuple, value: int) -> None:
        """Запись значения в игровое поле. 1 = нолик, 2 = крестик."""
        if key[0] > 2 or key[1] > 2 or not isinstance(key[0], int) or not isinstance(key[1], int):
            raise IndexError('неверный индекс клетки')
        if not bool(self.pole[key[0]][key[1]]):
            raise ValueError('клетка уже занята')
        else:
            self.pole[key[0]][key[1]].is_free = False
            self.pole[key[0]][key[1]].value = value

    def clear(self) -> None:
        """Функция очистки игрового поля."""
        self.__init__()

    def show(self) -> list:
        """Функция показа игрового поля."""
        return [[i.value for i in j] for j in self.pole]


class Cell:
    """Класс для описания ячейки игрового поля."""
    def __init__(self) -> None:
        self.is_free = True
        self.value = 0

    def __bool__(self) -> bool:
        return self.is_free




"""Задание из курса по ООП 3.8.12"""

class Cell:
    """Класс, для хранеения данных из ячеек таблиц."""
    def __init__(self, value: any) -> None:
        self.value = value


class SparseTable:
    """Класс, моделирующий поведение таблицы."""
    def __init__(self) -> None:
        self.rows = 0
        self.cols = 0
        self.data = dict()

    def add_data(self, row: int, col: int, data: Cell) -> None:
        """Добавление новой ячейки в таблицу."""
        self.data[(row, col)] = data
        self.check_table()

    def remove_data(self, row: int, col: int) -> None:
        """Удаление ячейки из таблицы."""
        if (row, col) not in self.data:
            raise IndexError('ячейка с указанными индексами не существует')
        self.data.pop((row, col))
        self.check_table()

    def __getitem__(self, item: tuple):
        """Получение данных из существующей ячейки."""
        if item not in self.data:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.data[item].value

    def __setitem__(self, key: tuple, value: any):
        """Запись или изменение данных в таблице."""
        if key in self.data:
            self.data[key].value = value
        else:
            self.data[key] = Cell(value)
            self.check_table()

    def check_table(self) -> None:
        """Расчет максимального размера таблицы."""
        rows, cols = [], []
        for i in self.data:
            rows.append(i[0])
            cols.append(i[1])



"""Реализация игры в крестики-нолики с компьютером."""

import random


class Cell:
    """Класс для описания ячейки игрового поля."""
    def __init__(self) -> None:
        self.value = 0

    def __bool__(self) -> bool:
        return not bool(self.value)


class TicTacToe:
    """Класс, моделирующий поведение игрового поля для игры в крестики-нолики."""
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self) -> None:
        """Создание игрового поля для игры в крестики-нолики."""
        self.pole = tuple([Cell() for _ in range(3)] for _ in range(3))
        self.count_step = 0
        self.__is_draw = False
        self.__is_computer_win = False
        self.__is_human_win = False

    def __getitem__(self, item: tuple) -> any((tuple, int)):
        """Функция для показа значений клеток игрового поля."""
        if self.check_index(item[0]) and self.check_index(item[1]):
            return self.pole[item[0]][item[1]].value

    def __setitem__(self, key: tuple, value: int) -> None:
        """Запись значения в игровое поле. 1 = крестик, 2 = нолик."""
        if self.check_index(key[0]) and self.check_index(key[1]):
            if bool(self.pole[key[0]][key[1]]):
                self.pole[key[0]][key[1]].value = value
                self.check_win()
                if self.count_step == 9 and not self.check_win():
                    self.is_draw = True

    def __bool__(self):
        if True in (self.__is_draw, self.__is_human_win, self.__is_computer_win):
            return False
        return True

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, new):
        self.__is_draw = new

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, new):
        self.__is_computer_win = new

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, new):
        self.__is_human_win = new

    @staticmethod
    def check_index(index):
        if 0 <= index < 3 and isinstance(index, int):
            return True
        raise IndexError('некорректно указанные индексы')

    def init(self) -> None:
        """Функция для запуска игры."""
        self.__init__()

    def show(self) -> list:
        """Функция показа игрового поля."""
        return [[i.value for i in j] for j in self.pole]

    def human_go(self) -> None:
        """Функция для хода игрока."""
        self.count_step += 1
        self.__setitem__(tuple(int(i) for i in input().split(' ')), self.HUMAN_X)

    def computer_go(self) -> None:
        """Функция для хода компьютера."""
        self.count_step += 1
        _ = (0, 1, 2)
        row, col = random.choice(_), random.choice(_)
        if bool(self.pole[row][col]):
            self.__setitem__((row, col), self.COMPUTER_O)
            return
        else:
            self.computer_go()

    def check_win(self):
        check_list = [set([self.pole[0][0].value, self.pole[0][1].value, self.pole[0][2].value]),
                      set([self.pole[1][0].value, self.pole[1][1].value, self.pole[1][2].value]),
                      set([self.pole[2][0].value, self.pole[2][1].value, self.pole[2][2].value]),
                      set([self.pole[0][0].value, self.pole[1][0].value, self.pole[2][0].value]),
                      set([self.pole[0][1].value, self.pole[1][1].value, self.pole[2][1].value]),
                      set([self.pole[0][2].value, self.pole[1][2].value, self.pole[2][2].value]),
                      set([self.pole[0][0].value, self.pole[1][1].value, self.pole[2][2].value]),
                      set([self.pole[0][2].value, self.pole[1][1].value, self.pole[2][0].value])]

        if {1} in check_list:
            self.__is_human_win = True
            return
        if {2} in check_list:
            self.__is_computer_win = True
            return
        else:
            return


        self.rows, self.cols = max(rows)+1, max(cols)+1
        
