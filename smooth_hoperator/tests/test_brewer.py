import unittest
from models.beer import Beer
from models.brewer import Brewer


class TestBrewer(unittest.TestCase):
    def setUp(self):
        self.brewer1 = Brewer(
            'Test Brewery', 'This brewery does not brew much really')
        self.beer1 = Beer('Django Dubbel', 'Strong Belgian Beer',
                          'Dubbel', 10, 2.49, 3.99, self.brewer1)
        self.beer2 = Beer('Python Pilsner', 'Light, inoffenseive, easy to drink',
                          'Pilsner', 25, 1.75, 2.99, self.brewer1)
        self.beer3 = Beer('C++ Saison', 'Complex flavours, hangover inducing fruity Saison',
                          'Saison', 4, 2.65, 3.75, self.brewer1)

    def test_brewer_has_name(self):
        self.assertEqual("Test Brewery", self.brewer1.name)

    def test_brewer_has_description(self):
        self.assertEqual("This brewery does not brew much really",
                         self.brewer1.description)
