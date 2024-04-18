from nqrduck.module.module import Module
# If the module is called "duck" the following line would be:
# from .model import DuckModel
from .model import ModuleModel
# If the module is called "duck" the following line would be:
# from .view import DuckView
from .view import ModuleView
# If the module is called "duck" the following line would be:
# from .controller import DuckController
from .controller import ModuleController

# If the module is called "duck" the following line would be:
# Duck = Module(DuckModel, DuckView, DuckController)
module = Module(ModuleModel, ModuleView, ModuleController)