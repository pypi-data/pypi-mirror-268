from . import _version

from .gwtc_update_pipeline_gevents import main as gwtc_update_pipeline_gevents
from .gwtc_diff import main as gwtc_diff
from .gwtc_get_gevent_coinc_files import main as gwtc_get_gevent_coinc_files
from .gwtc_create_from_query import main as gwtc_create_from_query

__version__ = _version.__version__
