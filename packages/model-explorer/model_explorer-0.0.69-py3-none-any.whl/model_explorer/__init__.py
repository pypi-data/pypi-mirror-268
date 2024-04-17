from importlib.metadata import version

from .adapter import Adapter, AdapterMetadata
from .consts import PACKAGE_NAME
from .graph import Graph, GraphNode, IncomingEdge
from .server import start
from .importers import import_pytorch, import_pytorch_and_start

# Default 'exports'.
#
# This allow users to do:
#
# import model_explorer
# model_explorer.start()
__all__ = ['start', 'Adapter', 'AdapterMetadata',
           'Graph', 'GraphNode', 'IncomingEdge',
           'import_pytorch', 'import_pytorch_and_start']

__version__ = version(PACKAGE_NAME)
