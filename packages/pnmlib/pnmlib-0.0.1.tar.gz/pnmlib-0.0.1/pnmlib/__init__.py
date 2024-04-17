r"""

"""
import numpy as _np

# This is a setting recipe from stackoverflow, not sure if it will work
class Settings:
    __conf = {
      "username": "",
      "password": "",
      "MYSQL_PORT": 3306,
      "MYSQL_DATABASE": 'mydb',
      "MYSQL_DATABASE_TABLES": ['tb_users', 'tb_groups']
    }
    __setters = ["username", "password"]

    @staticmethod
    def config(name):
        return Settings.__conf[name]

    @staticmethod
    def set(name, value):
        if name in Settings.__setters:
            Settings.__conf[name] = value
        else:
            raise NameError("Name not accepted in set() method")

    @staticmethod
    def show():
        from pprint import pprint
        pprint(Settings.__conf)


settings = {}
settings['missing_values'] = {'bool': False,
                              'int': _np.nan,
                              'float': _np.nan,
                              'object': None}


_reserved_prefixes = ['pore', 'throat', 'param', 'attr', 'conduit']
_reserved_delimiters = ['.', '@', '/', '|']

from . import utils
from . import generators
from . import io
from . import operations
from . import queries
from . import simulations
from . import tools
from . import visualization
from . import models
from . import core
from . import inspect
from .tools import get_edge_prefix
from .tools import get_node_prefix
