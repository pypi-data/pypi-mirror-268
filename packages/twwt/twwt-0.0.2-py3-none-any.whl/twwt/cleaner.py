
class TextCleaner:

    def __init__(
            self,
            parentheses: bool = False,
            punctuation: bool = False,
            gap: bool = False,
            qmark: bool = False,
            symbols: bool = False,
            math: bool = False,
            custom: list[str] | tuple[str] | set[str] | None = None
    ):
        """
        Класс, предоставляющий методы для удаления из текста
        предустановленных наборов символов или произвольного набора символов.


        Параметры определяют какие ноборы символов будут удалены
        из строки переданной в метод clean()

        Для произвольного набора задайте передайте в параметр custom последовательность (list, set, tuple) содержащую
        необходимые символы, слова (str).
        Например: TextCleaner(custom=["!", "^", ":"])

        Для инициализированного экземпляра параметры можно переопределить через метод set_config()

        :param parentheses: символы (){}[]
        :param punctuation: символы ,.!?:;
        :param gap: символы табуляции и переноса строки
        :param qmark: символы '"«»
        :param symbols: символы &^%$#@~
        :param math: символы -+=*/><
        :param custom: пользовательский набор символов
        """
        if self.__validate_attributes(parentheses, punctuation, gap, qmark, symbols, math, custom):
            self.__parentheses = parentheses
            self.__punctuation = punctuation
            self.__gap = gap
            self.__qmark = qmark
            self.__symbols = symbols
            self.__math = math
            self.__custom = custom
            self.__characters_to_delete: set[str] = self.__get_characters_to_delete()

    def __get_characters_to_delete(self) -> set[str]:
        characters = set()
        if self.__parentheses:
            characters.update(["(", "{", "[", "]", "}", ")"])
        if self.__punctuation:
            characters.update([",", ".", "!", "?", ":", ";"])
        if self.__gap:
            characters.update(["\n", "\t"])
        if self.__qmark:
            characters.update(["'", '"', "«", "»"])
        if self.__symbols:
            characters.update(["&", "^", "%", "$", "#", "@", "~", "\\"])
        if self.__math:
            characters.update(["-", "+", "=", "*", "/", ">", "<"])
        if self.__custom:
            for char in self.__custom:
                characters.add(char)
        return characters

    @staticmethod
    def __validate_attributes(
            parentheses,
            punctuation,
            gap,
            qmark,
            symbols,
            math,
            custom
    ) -> bool:
        for attribute in [parentheses, punctuation, gap, qmark, symbols, math]:
            if not isinstance(attribute, bool):
                raise TypeError(f"Не корректный тип аргумента {attribute=}. Ожидалось bool, получен {type(attribute)}")
        if custom is not None:
            if not isinstance(custom, set) and not isinstance(custom, list) and not isinstance(custom, tuple):
                raise TypeError(f"Не корректный тип аргумента custom. Ожидался один из: tuple, set, list. Получен {type(custom)}")
            if not all(isinstance(char, str) for char in custom):
                raise TypeError(f"В последовательности custom есть элемент с типом отличным от str")
        return True

    def set_config(
            self,
            parentheses: bool = False,
            punctuation: bool = False,
            gap: bool = False,
            qmark: bool = False,
            symbols: bool = False,
            math: bool = False,
            custom: str | list[str] | tuple[str] | None = None
    ) -> None:
        """
        Задать настройки для очистителя текста. Булево значение в параметре, отвечает за то
        какие группы символов будут удалены из входной строки переданной в метод clean()

        :param parentheses: символы (){}[]
        :param punctuation: символы ,.!?:;
        :param gap: символы табуляции и переноса строки
        :param qmark: символы '"«»
        :param symbols: символы &^%$#@~
        :param math: символы -+=*/><
        :param custom: пользовательский набор символов
        :return: None
        """
        if self.__validate_attributes(parentheses, punctuation, gap, qmark, symbols, math, custom):
            self.__parentheses = parentheses
            self.__punctuation = punctuation
            self.__gap = gap
            self.__qmark = qmark
            self.__symbols = symbols
            self.__math = math
            self.__custom = custom
            self.__characters_to_delete: set[str] = self.__get_characters_to_delete()

    @property
    def filters(self) -> set[str]:
        """Текущий перечень символов, которые будут удалены из строки переданной методу clean()"""
        return self.__characters_to_delete

    def clean(self, text: str) -> str:
        """
        Метод производящий очистку переданного текста от символов заданных в конфигурации

        :param text: произвольный текст
        :return: текст с удаленными символами
        """
        result = ""
        for char in text:
            if char not in self.__characters_to_delete:
                result += char
            else:
                continue
        return result
