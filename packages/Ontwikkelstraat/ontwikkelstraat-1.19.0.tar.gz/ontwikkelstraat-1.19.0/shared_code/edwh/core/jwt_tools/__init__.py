from .shared import *

try:
    from .jwt_web2py import *
except ImportError:
    ...

try:
    from .jwt_py4web import *
except ImportError:
    ...
