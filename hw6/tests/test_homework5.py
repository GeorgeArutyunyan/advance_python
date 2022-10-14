import unittest
from unittest.mock import patch
from hw6.data.example import documents, directories
from hw6.data.example import search_people, shelf, delete_items


class TestHw(unittest.TestCase):
    def test_search_people(self):
        with patch('builtins.input', result='11-2'):
            assert input() == '11-2'
            res = f'Владелец документа Геннадий Покемонов'
            self.assertMultiLineEqual(search_people(documents), res)

        with patch('builtins.input', result=''):
            assert input() == ''
            res = f'Документа с номером  не существует'
            self.assertMultiLineEqual(search_people(documents), res)

    def test_shelf(self):
        with patch('builtins.input', result='10006'):
            assert input() == '10006'
            res = f'Документ находится на полке № 2'
            self.assertMultiLineEqual(shelf(), res)

        with patch('builtins.input', result=''):
            assert input() == ''
            res = 'Такого номера нет в базе данных'
            self.assertMultiLineEqual(shelf(), res)

    def test_delete_items(self):
        with patch('builtins.input', result='2207 876234'):
            assert input() == '2207 876234'
            res = 'Документ 2207 876234 был удален'
            self.assertMultiLineEqual(delete_items(documents, directories), res)

        with patch('bultins.input', result=''):
            assert input() == ''
            res = f'Документа с номером  нет в базе данных'
            self.assertMultiLineEqual(delete_items(documents, directories), res)
