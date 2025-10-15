import importlib
import pkgutil
from flask import Blueprint

def register_routes(app):
    """
    Automatically imports and registers all Flask Blueprints 
    found under the app.routes package and its subpackages.
    """
    package_name = __name__

    for _, module_name, is_pkg in pkgutil.walk_packages(__path__, package_name + "."):
        if not is_pkg:
            module = importlib.import_module(module_name)
            # Look for any Blueprint instances in the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, Blueprint):
                    app.register_blueprint(attr)
                    print(f"✅ Registered blueprint: {attr.name} from {module_name}")
