from nqrduck.module.module_model import ModuleModel

# If the module is called "duck" the class would be called "DuckModel"

class ModuleModel(ModuleModel):

    def __init__(self, module):
        """Initialize the model."""
        super().__init__(module)