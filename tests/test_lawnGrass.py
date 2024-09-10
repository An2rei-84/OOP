
from src.lawnGrass import LawnGrass
import unittest


class TestLawnGrass(unittest.TestCase):
    def test_lawn_grass_name(self):
        lawn_grass = LawnGrass("Трава газонная", "Описание травы", 0, 1, "Страна", 7, "Цвет")
        result = lawn_grass.name
        self.assertEqual(result, "Трава газонная")
