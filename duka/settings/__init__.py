from .base import *


try:
    from .develpoment import *
except:
    from .production import *

if 'TRAVIS' in os.environ:
    from .ci import *