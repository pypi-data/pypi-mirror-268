from abc import abstractmethod
import os
import importlib
import inspect

import yaml


class Module:
    def __init__(self):
        pass

    @abstractmethod
    def setup(self) -> bool:
        pass

    @abstractmethod
    def has_credentials(self) -> bool:
        pass

    @abstractmethod
    def ask_credentials(self) -> bool:
        pass

    @abstractmethod
    def pre_run(self) -> bool:
        pass

    @abstractmethod
    def run(self) -> bool:
        pass

    @abstractmethod
    def post_run(self) -> bool:
        pass


def get_modules():
    """
    This function iterates through the 'dero-modules' directories and checks for the presence of a module.yml file.

    :return: A list of valid module names and path to their respective module files.
    """

    valid_modules = []
    modules_dir = os.path.join(os.path.dirname(__file__), 'dero-modules')
    print(f"Looking for modules in: {modules_dir}..\n")
    for module_dir in os.listdir(modules_dir):
        module_dir = os.path.join(modules_dir, module_dir)
        if os.path.isdir(module_dir):
            try:
                module_yml = os.path.join(module_dir, "module.yml")
                if os.path.isfile(module_yml):
                    with open(module_yml, 'r') as file:
                        yml_content = yaml.safe_load(file)
                        module_file = os.path.join(module_dir, yml_content.get("module_file"))
                        valid_modules.append({
                            "dir": module_dir,
                            "module_file_abs": module_file,
                            "module_file": yml_content.get("module_file"),
                            "name": yml_content.get("name"),
                            "description": yml_content.get("description"),
                            "version": yml_content.get("version"),
                            "author": yml_content.get("author"),
                            "author_email": yml_content.get("author_email")
                        })
            except Exception as ex:
                print("Skipping module: ", module_dir, ex)
                continue

    return valid_modules


def get_module_names(module_list):
    """
    This function returns a list of valid module names.

    :param module_list: A list of dictionaries, each representing a module.
    :return: A list of valid module names.
    """
    return [f"{module.get("name") or "unnamed module"}" for module in module_list]


def load_module(module: str):
    """
    This function loads a module from the given module name.
    :param module: The module to load.
    :return: The class of the loaded module.
    """
    module = module.replace(os.sep, ".").split(os.path.splitext(module)[1])[0]
    module_file = importlib.import_module(module)
    for name, obj in inspect.getmembers(module_file):
        if inspect.isclass(obj) and issubclass(obj, Module) and obj is not Module:
            return obj
