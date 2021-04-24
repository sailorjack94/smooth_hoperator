import pdb
from models.beer import Beer
from models.brewer import Brewer
import repositories.brewer_repository as brewer_repository
import repositories.beer_repository as beer_repository


pdb.set_trace()
brewer_repository.delete_all()
beer_repository.delete_all()

brewer1 = Brewer('Fallen Brewing', "Unrefined, Vegan friendly beer from Glasgow. Made with 100% renewable energy.")
brewer_repository.save(brewer1)

beer1 = Beer("Chew Chew", "Sweet, chewy stout with sugar.", "Stout", 15, 2.50, 3.10, brewer1)
beer_repository.save(beer1)