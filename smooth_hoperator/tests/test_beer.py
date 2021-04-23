import unittest
from models.beer import Beer 
from models.brewer import Brewer 

class TestBeer(unittest.TestCase):
    def setUp(self):
        self.brewer1 = Brewer('Test Brewery', 'This brewery does not brew much really')
        self.beer1 = Beer('Django Dubbel', 'Strong Belgian Beer', 'Dubbel', 2.49, 3.99, self.brewer1)
        self.beer2 = Beer('Python Pilsner', 'Light, inoffenseive, easy to drink', 'Pilsner', 1.75, 2.99, self.brewer1)
        self.beer3 = Beer('C++ Saison', 'Complex flavours, hangover inducing fruity Saison', 'Saison', 2.65, 3.75, self.brewer1)


    def test_beer_has_name(self):
        self.assertEqual('Django Dubbel', self.beer1.name)

    def test_beer_has_description(self):
        self.assertEqual('Strong Belgian Beer', self.beer1.description)

    def test_product_has_buy_price(self):
        self.assertEqual(2.65, self.beer3.buy_price)