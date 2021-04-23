import pdb
from models.beer import Beer
from models.brewer import Brewer
import repositories.brewer_repository as brewer_repository

brewer_repository.delete_all()

brewer1 = Brewer('Fallen Brewing', "Unrefined, Vegan friendly beer from Glasgow. Made with 100% renewable energy.")
brewer_repository.save(brewer1)