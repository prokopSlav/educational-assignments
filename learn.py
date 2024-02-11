"""Задание: написать класс с функциями, проверяющими передаваемые данные с пластиковых карт.
Формат ХХХХ-ХХХХ-ХХХХ-ХХХХ для номера карты и строка с именем и фамилей, разделенной через пробел."""


from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        number = number.split('-')
        try:
            x = [i for i in number if type(int(i)) is int and len(i) == 4]
            if len(x) == 4:
                return True
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def check_name(name):
        name = name.split(' ')
        result = []
        if len(name) == 2:
            for i in name:
                x = set(i).issubset(CardCheck.CHARS_FOR_NAME)
                result.append(x)

            if all(result) is True:
                return True
            else:
                return False
        else:
            return False


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
