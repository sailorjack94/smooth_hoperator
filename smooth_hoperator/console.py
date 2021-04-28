import pdb
from models.beer import Beer
from models.brewer import Brewer
import repositories.brewer_repository as brewer_repository
import repositories.beer_repository as beer_repository

brewer_repository.delete_all()
beer_repository.delete_all()

brewer1 = Brewer('Fallen Brewing',
                 "Unrefined, Vegan friendly beer from Glasgow. Made with 100% renewable energy.")
brewer_repository.save(brewer1)
brewer2 = Brewer('Harviestoun Brewery',
                 'Established brewery using ingredients from the Scottish Highlands.')
brewer_repository.save(brewer2)


beer1 = Beer("Chew Chew", "Sweet, chewy stout with sugar.",
             "Stout", 15, 2.50, 3.10, brewer1)
beer_repository.save(beer1)
beer2 = Beer('Schiehallion', 'Crisp lager with refreshing notes.',
             'Lager', 25, 1.90, 3.50, brewer2)
beer_repository.save(beer2)
beer3 = Beer('Bitter and Twisted', 'Sweet malt and bitter hops in one bottle. Full bodied light ale style with a punch.',
             'Golden Ale', 10, 1.75, 3.00, brewer2)
beer_repository.save(beer3)
