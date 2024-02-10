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

