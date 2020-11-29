from unittest import TestCase
from unittest.mock import patch

from pythonApp import Animal


class TestAnimal(TestCase):

    def setUp(self):
        self.a = Animal('test_name', 'test_sound')

    def test_second(self):
        pass

    def test_third__two(self):
        pass

    def test_fourth__one(self):
        pass

    def test_animal_creation(self):
        self.assertEqual(self.a.name, 'test_name')
        self.assertEqual(self.a.sound, 'test_sound')

    def test_animal_makes_sound(self):
        with patch('builtins.print') as mocked_print:
            self.a.make_sound()
            mocked_print.assert_called_with('test_name makes "test_sound"')

    def test_animal_has_make_sound_method(self):
        with patch('pythonApp.Animal.make_sound') as mocked_make_sound:
            mocked_make_sound.return_value = 'returnedValue'
            val = self.a.make_sound()

            mocked_make_sound.assert_called()
            self.assertEqual(val, 'returnedValue')